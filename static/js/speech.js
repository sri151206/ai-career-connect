/**
 * speech.js — Browser-side speech recording & TTS playback
 * =========================================================
 * WHY THIS FILE EXISTS:
 *   Handles the MediaRecorder API for capturing voice input (STT)
 *   and fetching synthesised audio from the /speech/to-speech
 *   endpoint (TTS). Keeps speech logic separate from page scripts.
 */

document.addEventListener('DOMContentLoaded', () => {

    // ── Voice Recording (STT) ────────────────────────────────
    const recordBtn = document.getElementById('voice-record-btn');
    const voiceStatus = document.getElementById('voice-status');

    if (recordBtn) {
        let mediaRecorder = null;
        let audioChunks = [];
        let isRecording = false;

        recordBtn.addEventListener('click', async () => {
            if (!isRecording) {
                // Start recording
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                    mediaRecorder = new MediaRecorder(stream);
                    audioChunks = [];

                    mediaRecorder.ondataavailable = (e) => audioChunks.push(e.data);
                    mediaRecorder.onstop = async () => {
                        const blob = new Blob(audioChunks, { type: 'audio/webm' });
                        const formData = new FormData();
                        formData.append('audio', blob, 'recording.webm');

                        voiceStatus.textContent = 'Transcribing…';
                        try {
                            const res = await fetch('/speech/to-text', { method: 'POST', body: formData });
                            const data = await res.json();
                            if (data.text) {
                                const skillsInput = document.getElementById('skills');
                                if (skillsInput) skillsInput.value = data.text;
                                voiceStatus.textContent = 'Transcription complete!';
                            } else {
                                voiceStatus.textContent = data.error || 'Transcription failed.';
                            }
                        } catch (err) {
                            voiceStatus.textContent = 'Error sending audio.';
                        }
                    };

                    mediaRecorder.start();
                    isRecording = true;
                    recordBtn.textContent = '⏹ Stop Recording';
                    voiceStatus.textContent = 'Recording…';
                } catch (err) {
                    voiceStatus.textContent = 'Microphone access denied.';
                }
            } else {
                // Stop recording
                mediaRecorder.stop();
                isRecording = false;
                recordBtn.textContent = 'Start Recording';
            }
        });
    }

    // ── Read Aloud (TTS) ─────────────────────────────────────
    const readBtn = document.getElementById('read-aloud-btn');
    if (readBtn) {
        readBtn.addEventListener('click', async () => {
            const text = document.querySelector('.recommendation-text')?.textContent;
            if (!text) return;

            readBtn.textContent = '⏳ Generating audio…';
            readBtn.disabled = true;

            try {
                const res = await fetch('/speech/to-speech', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text }),
                });
                const blob = await res.blob();
                const url = URL.createObjectURL(blob);
                const audio = new Audio(url);
                audio.play();
                readBtn.textContent = '🔊 Read Aloud';
            } catch (err) {
                readBtn.textContent = '❌ Audio failed';
            } finally {
                readBtn.disabled = false;
            }
        });
    }
});
