# Snake and Ladder Game

A Flask-based Snake and Ladder game demonstrating AI concepts (e.g., ladders as correct diagnoses, snakes as errors).

## Setup
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install dependencies: `pip install -r requirements.txt`
5. Run locally: `python app.py` or deploy with `gunicorn -w 4 -b 0.0.0.0:8000 app:app`
6. Access at `http://localhost:5000` (or port 8000 for Gunicorn).

## Files
- `app.py`: Flask app with game logic.
- `templates/index.html`: Main game interface.
- `templates/result.html`: Result page.
- `static/css/style.css`: Styles for HTML pages.
- `static/js/script.js`: Client-side JavaScript.
- `requirements.txt`: Dependencies (Flask, Gunicorn).
- `Procfile`: For Heroku deployment.

## Usage
- Click "Roll Dice" to play a turn (human and computer).
- Game redirects to result page when a player reaches 100.
- Click "Play Again" to restart.
