# 🚀 AI Career Connect — Beginner-Friendly Guide

Welcome to **AI Career Connect**! This is a web application designed to help people find their dream careers using artificial intelligence. 

If you are new to programming or web development, this guide will explain how the project works, why we structured it this way, and how you can run it on your own computer.

---

## 🌟 What Does This App Do?

Imagine you want career advice but don't know who to ask. This application allows you to:
1. **Sign Up & Log In**: Create a personal account.
2. **Type or Speak Your Skills**: Input what you know (e.g., "Python, writing, design") either by typing or **speaking into your microphone**.
3. **Get Expert AI Advice**: The app sends your information to a smart AI called **Mistral AI**, which returns a personalized career recommendation and learning path.
4. **Listen to the Advice**: Click a button to **hear the AI read its advice out loud**!
5. **View Your Dashboard**: See charts and stats showing your history and which skills you use the most.

---

## 🛠️ The Tech Stack (The Tools We Used)

We built this app using Python and a few other standard tools:

* **Flask (The Engine)**: Flask is a simple tool in Python that lets us build websites. It handles requests when you click on links and decides what to show on your screen.
* **SQLite (The Notebook)**: A lightweight database. It acts like a digital Excel sheet or notebook where the app saves user passwords, career analyses, and chat messages.
* **SQLAlchemy (The Translator)**: A tool that lets Python talk to our SQLite database using simple Python code instead of complex database commands.
* **Mistral AI (The Brain)**: A powerful Artificial Intelligence system. We send your skills to it, and it writes back with professional career paths.
* **SpeechRecognition (The Ears)**: Translates your recorded voice into text.
* **gTTS / Google Text-to-Speech (The Voice)**: Translates written text into spoken audio.
* **Chart.js (The Artist)**: A JavaScript library that draws beautiful bar charts on your dashboard.

---

## 📂 Project Structure Explained in Simple Words

Here is how the project files are organized and why:

```text
ai_carrer_connect/
├── run.py                 # The green "START" button. Double-click or run this to start the website.
├── config.py              # The settings book. Stores database paths, API keys, and secret values.
├── requirements.txt       # The shopping list. Lists all the Python helper packages this app needs to work.
├── .env.example           # A template showing what secret keys (like Mistral API keys) you need to set up.
│
├── app/                   # 🏗️ The main kitchen where everything is cooked.
│   ├── __init__.py        # The coordinator. Sets up Flask and connects the database and web pages.
│   │
│   ├── models/            # 💾 Database files (what the database remembers).
│   │   ├── user.py        # Remembers username, email, and password.
│   │   ├── career_profile.py # Remembers your skills, interests, and the AI's recommendations.
│   │   └── chat_history.py   # Remembers past chat messages between you and the AI.
│   │
│   ├── routes/            # 🌐 The roadmap (directs you to different pages).
│   │   ├── main.py        # Handles the welcome home page and about page.
│   │   ├── auth.py        # Handles register, login, and logout.
│   │   ├── career.py      # Handles the career input form and AI advice generator.
│   │   ├── dashboard.py   # Handles your profile page and stats graphs.
│   │   └── speech.py      # Handles translating speech to text and text to speech.
│   │
│   ├── services/          # ⚙️ Helper services (interacts with the outside world).
│   │   ├── mistral_service.py # Talks to the Mistral AI system.
│   │   └── speech_service.py  # Handles recording translation and speaking translation.
│   │
│   └── utils/             # 🔧 Toolbox. Contains small helper tools used in multiple places.
│
├── templates/             # 📄 The skeleton HTML files (coloring book pages).
│   │                      # These are web pages with empty spaces that Flask fills in dynamically.
│   ├── base.html          # The master layout (has the navigation bar that appears on every page).
│   ├── index.html         # The landing/welcome home page.
│   ├── career/
│   │   ├── analyze.html   # The page where you type your skills or record your voice.
│   │   └── result.html    # The page showing the AI's suggestions and the "Read Aloud" button.
│   └── dashboard/
│       └── index.html     # The dashboard page that contains your charts.
│
├── static/                # 🎨 Static assets (the paint and cosmetics).
│   ├── css/
│   │   └── style.css      # The stylesheet. Contains dark-mode styles, fonts, and button colors.
│   └── js/
│       ├── main.js        # Runs background actions (like hiding pop-ups after a few seconds).
│       ├── dashboard.js   # Asks the database for stats and draws the Chart.js graphs.
│       └── speech.js      # Controls your microphone and audio player.
│
└── tests/                 # 🧪 The test lab. Helper scripts to ensure code works properly.
```

---

## ⚡ How to Setup and Run (For Beginners)

Follow these simple steps to run this project on your Windows computer:

### Step 1: Install Python
Ensure Python is installed on your computer. You can download it from [python.org](https://www.python.org/). Make sure to check the box that says **"Add Python to PATH"** during installation.

### Step 2: Open Terminal / Command Prompt
Open the folder where you saved this project, click on the address bar at the top, type `cmd`, and press **Enter**. This opens a command window pointing to your project.

### Step 3: Create a Virtual Environment
A virtual environment is like a private workspace so this project's packages don't interfere with other Python programs on your computer. Run:
```bash
python -m venv venv
```

### Step 4: Activate the Workspace
Tell your computer to use this private environment:
```bash
venv\Scripts\activate
```
*(You will see `(venv)` appear at the beginning of your line in command prompt.)*

### Step 5: Install the Required Packages
Download and install Flask and other libraries listed in our requirements file:
```bash
pip install -r requirements.txt
```

### Step 6: Add Your Secret Keys
1. In your project folder, copy the file named `.env.example` and rename the copy to `.env`.
2. Open `.env` in a text editor (like Notepad).
3. Put your unique **Mistral AI API Key** next to `MISTRAL_API_KEY=`. It should look like this:
   ```env
   MISTRAL_API_KEY=your_real_key_goes_here
   ```

### Step 7: Launch the App!
Run this command to turn on the website:
```bash
python run.py
```
You will see output saying `Running on http://127.0.0.1:5000`.

Open your web browser (Chrome, Edge, or Firefox) and visit **`http://127.0.0.1:5000`** to start using the app!
