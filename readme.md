
# Memory Game

A Python Turtle-based memory game where players repeat patterns of turtle clicks. Each round, the pattern grows longer, testing your memory. Scores are tracked and the top 10 are saved in a local leaderboard using SQLite.

## Features

- Four clickable turtles, each with unique colors and positions 
- Visual feedback for pattern playback and user clicks
- Score display and leaderboard
- Prompts for player name on game over

## How to Play

1. Watch the pattern played by the game.
2. Repeat the pattern by clicking the turtles in the correct order.
3. Each round adds a new step to the pattern.
4. The game ends when you make a mistake. Your score is added to the leaderboard.

## Requirements

- Python 3.x
- Turtle graphics (included with Python)
- SQLite3 (included with Python)

## Running the Game

Run `turtleGame.py` in your Python environment. Ensure the required image files are present in the `images` folder as referenced in the script. 

You will HAVE to create a Database named leaderBoard.db. The easiest way to do this is to replace the code in `if \_\_name__ == "\_\_main__":` with `leaderboardUpdate("John Smith", 0)` then run then change back to `main()`

## Notes

I did create the majority of this readme with my VSCode Github AI Chat. I did not use it to create my program, though it did help with some bug fixes. Any ideas to simplfy this would be greatly appreciated. You can replace the images with pretty much anything... the leaderboard is local though, so you may have to create a db for it to work correctly
