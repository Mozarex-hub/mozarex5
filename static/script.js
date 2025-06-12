function rollDice() {
    fetch('/roll')
        .then(response => response.json())
        .then(data => {
            document.getElementById("dice-result").innerText = "You rolled a " + data.dice_value + "!";
        });
}
