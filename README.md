# Answer The Monster

 Answer The Monster application is an interactive desktop quiz game that challenges players to answer questions within a time limit. The game features a clean and intuitive chat format interface. It also has real-time scoring and persistent score tracking.

## Features

- **Character Creation**: Create and name your own game character
- **Chat Format Interface** : The questions are asked and answers recieved in chat format.
- **Timed Gameplay**: 10-second countdown timer for each question
- **Score Tracking**: Real-time score updates with point tracking
- **Scores and Result Display**: View scores and game result for each game

## Technology Stack

- **Python** : 3.13.1
- **Tkinter** : 8.6
- **SQLite3** : 3.37.0

## Installation

For macOS and Ubuntu/Debian
```bash
python3 answer_the_monster_app.py
```

For windows
```bash
python answer_the_monster_app.py
```

That's it! No additional dependencies to install.

### Verify tkinter Installation

For macOS and windows, Tkinter is included with python. For Ubuntu/Debian, verify first using

```bash
python3 -m tkinter
```

This should open a small test window. If it doesn't work, install tkinter:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

## How to Play

1. **Start the Game**: Launch the application with `python3 answer_the_monster_app.py`<br>
(For windows `python answer_the_monster_app.py`)

2. **Main Menu**: Choose New Game from the three given options:
   - New Game
   - Scores
   - Exit

3. **Create Character**: Enter your player name (no special characters allowed).

4. **Answer Questions**:
   - Give a positive response (yes, yeah, etc.) to start the game.
   - Click on any of the buttons. From any one, a monster will pop up randomly. He will ask you a question.
   - Read the question carefully.
   - Type your answer in the input box.
   - You have 10 seconds per question.
   - For correct answer you gain monster's 5 points and for incorrect answers monster gains your 5 points.
   - Both start at 50 points. Whoever's points first become zero loses.

5. **View Results**: Check your score and compare with previous games by choosing Scores option in main menu.

## Project Structure

```
Answer_The_Monster/
├── answer_the_monster_app.py    # Main application entry point
├── database/                    # Database operations
├── game/                        # Core game logic
├── options/                     # Game configuration
├── widgets/                     # UI components
|── scroll/                      # Code to enable scrolling
|── README.md
```