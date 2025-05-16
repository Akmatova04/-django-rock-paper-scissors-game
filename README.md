
# ✊🖐✌️ Django "Rock, Paper, Scissors" Game

A classic **Rock, Paper, Scissors** game built with Django. The user plays against the computer.

---

## 🎯 Purpose

To demonstrate Django fundamentals:

* Views, Templates, URLs
* Forms & Sessions
* Simple game logic and score tracking

---

## 🛠️ Technologies

* Python 3 🐍
* Django 5.x 🌐

---

## ⚙️ How to Run

```bash
git clone 
cd django_rps_game_project

python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open 👉 `http://127.0.0.1:8000/rps/play/`

---

## 🧩 Game Logic

* User selects **Rock**, **Paper**, or **Scissors**
* Computer randomly picks one
* Result is shown: **Win**, **Lose**, or **Draw**
* Scores are stored in session data
* "Reset Scores" button clears the scores

---

## 📁 Key Components

* `views.py` — game & reset logic
* `urls.py` — routes setup
* `play_rps_template.html` — game interface
* `settings.py` — project config

