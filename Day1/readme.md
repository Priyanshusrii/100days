## Overview
A simple command-line game where the program randomly selects a number within a defined range, and the user tries to guess it. After each guess, the program provides feedback on whether the guess was too high or too low, until the correct number is found.

## Features
- Randomly generated target number within a specified range
- Real-time feedback after each guess (too high / too low)
- Tracks and displays the total number of attempts
- Input validation to handle non-numeric or out-of-range entries
- Option to replay the game without restarting the program

## Concepts Used
- Python `random` module
- Loops and conditional statements
- Exception handling (`try`/`except`)
- Basic input/output operations

## How to Run
1. Make sure Python 3.x is installed on your system.
2. Navigate to this folder in your terminal.
3. Run the script:
```bash
   python main.py
```
4. Follow the on-screen prompts to guess the number.

## Sample Usage
```
Guess the number between 1 and 100: 50
Too high! Try again.
Guess the number between 1 and 100: 25
Too low! Try again.
Guess the number between 1 and 100: 37
Correct! You guessed it in 3 attempts.
```