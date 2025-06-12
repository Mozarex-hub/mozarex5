from flask import Flask, jsonify
import random

app = Flask(__name__)

# Define the board with snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

@app.route("/")
def home():
    return "Welcome to Snake and Ladder! Use /roll to roll the dice."

@app.route("/roll")
def roll():
    dice_value = roll_dice()
    return jsonify({"dice_value": dice_value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
