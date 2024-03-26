# HackPython - Tetris Bot

### 👑This bot won the 2023 BEST/CECI Hackaton of the Catholic University of Louvain La Neuve👑


https://github.com/thomasdevl/HackaPython/assets/91684310/6ed92fac-ce6c-4dc8-9d36-071ef3f31254



## Description

This is a bot for the game Tetris.
It only works on [this website](https://web.itu.edu.tr/~msilgu/tetris/tetris.html)

## Demo

<img width="400" alt="Screenshot 2023-11-15 at 19 12 32" src="screenshots/game.gif">

Our higgest score is 10.5 million points.

<img width="400" alt="Screenshot 2023-11-15 at 19 12 32" src="screenshots/records.png">

## Installation

1. Install Python 3.6 or higher

2. Run the following command in the terminal:

```bash
pip install -r requirements.txt
```
We recommend running a python venv you can find info on how to launch one [here](https://docs.python.org/3/library/venv.html)

## Usage

1. Update the pixel values for the game in the `config.py` file.
### new_game_x, new_game_y
<img width="400" alt="newgame png" src="screenshots/newgame.png">

### first_piece_x, first_piece_y
<img width="400" alt="current piece png" src="screenshots/currentpiece.png">

### next_piece_x, next_piece_y
<img width="400" alt="next piece png" src="screenshots/nextpiece.png">

### accept_x, accept_y
<img width="400" alt="confirn png" src="screenshots/ok.png">

### game_over_x, game_over_y 
<img width="400" alt="game over png" src="screenshots/gameover.png">

2. Run the following command in the terminal:

```bash
python3 main.py
```

2*. if you get an error related to the self.color_to_piece dictionnary then you need to update the color values in the config.py.
