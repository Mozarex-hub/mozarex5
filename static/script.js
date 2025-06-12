async function rollDice() {
    const response = await fetch('/roll', { method: 'POST' });
    const data = await response.json();
    document.getElementById('human-position').textContent = data.human_position;
    document.getElementById('computer-position').textContent = data.human_position;
    document.getElementById('game-status').innerHTML = data.message.replace(/\n/g, '<br>');
    if (data.game_over) {
        document.querySelector('button').disabled = true;
    }
}
