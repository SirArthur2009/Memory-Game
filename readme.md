
# Memory Game

A Python Turtle-based memory game where players repeat patterns of turtle clicks. Each round, the pattern grows longer, testing your memory. Scores are tracked and the top 10 are saved in a local leaderboard using SQLite. 

## Features

- Four clickable turtles, each with unique colors and positions
- Visual feedback for pattern playback and user clicks
- Score display and leaderboard
- Prompts for player name on game over

## How to Play

1. Watch the pattern played by the game.
1. Repeat the pattern by clicking the turtles in the correct order.
1. Each round adds a new step to the pattern.
1. The game ends when you make a mistake. Your score is added to the leaderboard.

## Requirements

- Python 3.x
- Turtle graphics (included with Python)
- SQLite3 (included with Python)
- Pygame (for full functionality, but not technically required)

## Running the Game

Run `turtleGame.py` in your Python environment. Ensure the required image files are present in the `images` folder as referenced in the script.

## Versions

- Turtle import (Comes with Python)
- Pygame import (has to be installed)
  
  Pygame import version is not working yet

## Updates

### Already complete

- Added leaderboard to turtle version
- Start working on pygame version

### Future Updates

- Complete pygame version
- Add leaderboard to pygame version

## Notes

I did create the majority of this readme with my VSCode Github AI Chat. I did not use it to create my program, though it did help with some bug fixes. Any ideas to simplfy this would be greatly appreciated. You can replace the images with pretty much anything... 
