<!DOCTYPE html>
<html>
<head>
  <title>Dice Roller Upgrades</title>
</head>
<body>
  <h1>Dice Roller</h1>
  <p>Points: <span id="points">0</span></p>
  <p>Highest Dice Reached: <span id="highestDice"></span></p>
  <button id="rollButton">Roll Dice</button>
  <button id="linePrestigeButton" disabled>Line Prestige</button>
  <button id="squarePrestigeButton" disabled>Square Prestige</button>
  <div id="upgrades">
    <!-- Upgrade buttons will be added here -->
  </div>
  <div id="endMessage" style="display: none;">
    <p>You've reached the end of this prototype</p>
  </div>
  <script>
    const pointsElement = document.getElementById('points');
    const highestDiceElement = document.getElementById('highestDice');
    const rollButton = document.getElementById('rollButton');
    const linePrestigeButton = document.getElementById('linePrestigeButton');
    const squarePrestigeButton = document.getElementById('squarePrestigeButton');
    const upgradesContainer = document.getElementById('upgrades');
    const endMessage = document.getElementById('endMessage');

    let points = 0;
    let highestReached = 0;
    let rollValue = 1; // Initial roll value
    let upgrades = [
      { name: 'Double Roll Value', cost: 10, action: () => rollValue *= 2 },
      // Add more upgrades here
    ];

    function calculateDieNumber(points, n) {
      return (Math.floor(points / Math.pow(6, n)) % 6) + 1;
    }

    function updateUpgradeButtons() {
      upgradesContainer.innerHTML = '';
      upgrades.forEach((upgrade, index) => {
        const button = document.createElement('button');
        button.textContent = `${upgrade.name} - ${upgrade.cost} points`;
        button.addEventListener('click', () => buyUpgrade(index));
        upgradesContainer.appendChild(button);
      });
    }

    function buyUpgrade(index) {
      const upgrade = upgrades[index];
      if (points >= upgrade.cost) {
        points -= upgrade.cost;
        upgrade.cost = Math.round(upgrade.cost * 5.5);
        pointsElement.textContent = points;
        upgrade.action();
        updateUpgradeButtons();
      }
    }

    rollButton.addEventListener('click', () => {
      const rolledValue = Math.floor(Math.random() * 6) + 1;
      points += rolledValue * rollValue;
      pointsElement.textContent = points;

      for (let n = highestReached + 1; ; n++) {
        const dieValue = calculateDieNumber(points, n);
        if (dieValue >= 2) {
          highestReached = n;
        } else {
          break;
        }
      }

      highestDiceElement.textContent = `Highest Dice Reached: (Die ${highestReached + 1}) With A Value Of ${calculateDieNumber(points, highestReached)}`;
      
      if (highestReached >= 7 && calculateDieNumber(points, 7) === 6) {
        endMessage.style.display = 'block';
      } else {
        endMessage.style.display = 'none';
      }

      // Moved dicelineSquared and related code here
      const diceline = 2;
      const dicelineSquared = Math.pow(diceline, 2); // Calculate diceline squared
      if (highestReached >= dicelineSquared) {
        // Code to execute if the condition is met
        // For example, enable a button or display a message
        squarePrestigeButton.disabled = false; // Enable the square prestige button
      } else {
        squarePrestigeButton.disabled = true; // Disable the square prestige button
      }

      // Unlock the lineprestige button
      if ((calculateDieNumber(points, highestReached) === 6 && highestReached >= (diceline-1)) || (highestReached > (diceline-1) && highestReached < 6)) {
        linePrestigeButton.disabled = false;
      } else {
        linePrestigeButton.disabled = true;
      }

      updateUpgradeButtons();
    });

    linePrestigeButton.addEventListener('click', () => {
      // Implement the Line Prestige action here
      // For example, you can reset certain values or provide additional rewards
      alert("Congratulations! You've triggered Line Prestige!");
    });

    squarePrestigeButton.addEventListener('click', () => {
      const diceline = 2; // Sets the length of the cube
      if ((calculateDieNumber(points, highestReached) === 6 && highestReached >= 3) || (highestReached > 3 && highestReached < 6)) {
        // Implement the Square Prestige action here
        alert("Congratulations! You've triggered Square Prestige!");
      }
    });

    function updateSquarePrestigeButton() {
      const diceLine = 2;
      if ((calculateDieNumber(points, highestReached) === 6 && highestReached >= (dicelineSquared-1)) || (highestReached > (dicelineSquared-1) && highestReached < 6)) {
        squarePrestigeButton.disabled = false;
      } else {
        squarePrestigeButton.disabled = true;
      }
    }

    // Initial upgrade buttons setup
    updateUpgradeButtons();
  </script>
</body>
</html>
