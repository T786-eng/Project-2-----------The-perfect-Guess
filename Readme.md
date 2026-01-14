# Number Guessing Game 🎲

A Python command-line game where the player tries to guess a randomly generated number between 1 and 100. The game tracks your attempts and gives hints to guide you to the correct answer.

## 🛠️ Features
- **Random Number Generation:** The game picks a new number every time you run it.
- **Hint System:** Tells you if your guess should be higher or lower (check logic note below).
- **Score Tracking:** Counts how many attempts it took you to win.

## 🚀 How to Run

1. Make sure Python is installed.
2. Run the script:
   ```bash
   python main.py

📝 Example Output

Guess the number: 50

Higher Number please

Guess the number: 75

Lower Number please

Guess the number: 63

you have guessed the number 63 correctly in 3 attempt


⚙️ Logic
  
  The game uses a while loop to keep asking for input until the user's guess (a) matches the random number (n).
