const boardSize = 10; // 10x10 board
let positions = [1, 1]; // Player positions
let currentPlayer = 0; // 0 = Player 1, 1 = Player 2

const snakes = { 17: 7, 54: 34, 62: 19, 98: 79 };
const ladders = { 3: 22, 6: 25, 20: 38, 57: 76, 72: 91 };

function rollDice() {
    let diceRoll = Math.floor(Math.random() * 6) + 1;
    document.getElementById("dice-result").innerText = `Dice: 🎲 ${diceRoll}`;
    
    let newPosition = positions[currentPlayer] + diceRoll;
    
    if (newPosition <= 100) {
        positions[currentPlayer] = snakes[newPosition] || ladders[newPosition] || newPosition;
    }
    
    updatePlayerPosition();
    
    if (positions[currentPlayer] === 100) {
        alert(`Player ${currentPlayer + 1} wins!`);
        resetGame();
        return;
    }
    
    currentPlayer = currentPlayer === 0 ? 1 : 0;
    document.getElementById("turn-info").innerText = `Player ${currentPlayer + 1}'s Turn`;
}

function updatePlayerPosition() {
    let playerElement = document.getElementById(`player${currentPlayer + 1}`);
    let row = Math.floor((positions[currentPlayer] - 1) / boardSize);
    let col = (positions[currentPlayer] - 1) % boardSize;
    
    playerElement.style.bottom = `${row * 40}px`;
    playerElement.style.left = `${col * 40}px`;
}

function resetGame() {
    positions = [1, 1];
    currentPlayer = 0;
    document.getElementById("turn-info").innerText = "Player 1's Turn";
    updatePlayerPosition();
}
