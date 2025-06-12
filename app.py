import random
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# Game state
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
human_position = 0
computer_position = 0
game_over = False
last_message = ""

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice_value):
    new_position = position + dice_value
    if new_position > 100:
        return position, ""
    message = f"Moved to {new_position}. "
    if new_position in snakes:
        message += f"Oops! Bitten by a snake at {new_position}. Down to {snakes[new_position]}."
        new_position = snakes[new_position]
    elif new_position in ladders:
        message += f"Yay! Climbed a ladder at {new_position}. Up to {ladders[new_position]}."
        new_position = ladders[new_position]
    return new_position, message

@app.route('/')
def index():
    global human_position, computer_position, game_over, last_message
    # Reset game state for a new game
    human_position = 0
    computer_position = 0
    game_over = False
    last_message = ""
    return render_template('index.html')

@app.route('/roll', methods=['POST'])
def roll():
    global human_position, computer_position, game_over, last_message
    if game_over:
        winner = "You won!" if human_position == 100 else "Computer won!"
        return redirect(url_for('result', winner=winner, human_position=human_position, computer_position=computer_position, message=last_message))

    # Human's turn
    dice_value = roll_dice()
    message = f"You rolled a {dice_value}. "
    human_position, human_message = move_player(human_position, dice_value)
    message += human_message
    if human_position == 100:
        game_over = True
        message += "\n🎉 Congratulations! You won the game! 🎉"
        last_message = message
        return jsonify({
            'human_position': human_position,
            'computer_position': computer_position,
            'message': message,
            'game_over': True
        })

    # Computer's turn
    dice_value = roll_dice()
    message += f"\nComputer's turn: Rolled a {dice_value}. "
    computer_position, computer_message = move_player(computer_position, dice_value)
    message += computer_message
    if computer_position == 100:
        game_over = True
        message += "\n🤖 Computer wins! Better luck next time! 🤖"
    
    last_message = message
    return jsonify({
        'human_position': human_position,
        'computer_position': computer_position,
        'message': message,
        'game_over': game_over
    })

@app.route('/result')
def result():
    winner = request.args.get('winner')
    human_position = request.args.get('human_position')
    computer_position = request.args.get('computer_position')
    message = request.args.get('message').replace('\n', '<br>') if request.args.get('message') else ""
    return render_template('result.html', winner=winner, human_position=human_position, computer_position=computer_position, message=message)

if __name__ == '__main__':
    app.run(debug=True)
