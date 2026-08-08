/**
 * dashboard.js — Dynamic dashboard charts & stats
 * =================================================
 * WHY THIS FILE EXISTS:
 *   Fetches JSON data from /dashboard/api/stats and renders interactive
 *   Chart.js visualisations. Keeps chart logic out of templates.
 */

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const res = await fetch('/dashboard/api/stats');
        const data = await res.json();

        // ── Update stat cards ──────────────────────────────
        document.getElementById('stat-profiles-count').textContent = data.total_profiles;
        document.getElementById('stat-chats-count').textContent = data.total_chats;

        // ── Render skills bar chart ────────────────────────
        const labels = Object.keys(data.skill_counts);
        const values = Object.values(data.skill_counts);

        if (labels.length > 0) {
            const ctx = document.getElementById('skillsChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels,
                    datasets: [{
                        label: 'Skill Frequency',
                        data: values,
                        backgroundColor: 'hsla(170, 78%, 46%, 0.5)',
                        borderColor: 'hsl(170, 78%, 46%)',
                        borderWidth: 1,
                        borderRadius: 6,
                    }],
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { labels: { color: 'hsl(0, 0%, 93%)' } },
                    },
                    scales: {
                        x: { ticks: { color: 'hsl(230, 10%, 60%)' }, grid: { color: 'hsla(230, 15%, 22%, 0.5)' } },
                        y: { ticks: { color: 'hsl(230, 10%, 60%)' }, grid: { color: 'hsla(230, 15%, 22%, 0.5)' }, beginAtZero: true },
                    },
                },
            });
        }
    } catch (err) {
        console.error('Failed to load dashboard stats:', err);
    }
});
