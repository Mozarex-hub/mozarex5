import random

# Define the board with snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    """Simulates rolling a dice (1 to 6)."""
    return random.randint(1, 6)

def move_player(position, dice_value):
    """Moves the player based on dice roll and checks for snakes/ladders."""
    new_position = position + dice_value
    
    if new_position > 100:
        return position  # Stay in place if overshooting 100
    
    # Check for snakes or ladders
    if new_position in snakes:
        print(f"🐍 Oops! Bitten by a snake at {new_position}. Down to {snakes[new_position]}.")
        return snakes[new_position]
    elif new_position in ladders:
        print(f"🪜 Yay! Climbed a ladder at {new_position}. Up to {ladders[new_position]}.")
        return ladders[new_position]
    
    return new_position

def play_game():
    """Runs the Snake and Ladder game between a human and the computer."""
    human_position = 0
    computer_position = 0
    
    while True:
        input("\n🎲 Your turn! Press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value}.")
        human_position = move_player(human_position, dice_value)
        print(f"📍 Your new position: {human_position}")
        
        if human_position == 100:
            print("\n🎉 Congratulations! You won the game! 🎉")
            break
        
        # Computer's turn
        print("\n🤖 Computer's turn...")
        dice_value = roll_dice()
        print(f"Computer rolled a {dice_value}.")
        computer_position = move_player(computer_position, dice_value)
        print(f"📍 Computer's new position: {computer_position}")
        
        if computer_position == 100:
            print("\n🤖 Computer wins! Better luck next time! 🤖")
            break

if __name__ == "__main__":
    play_game()

