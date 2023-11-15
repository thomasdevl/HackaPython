HackPython - Tetis Bot

## Description

This is a bot for the game Tetris.
It only works on [this website](https://web.itu.edu.tr/~msilgu/tetris/tetris.html)

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
<img width="111" alt="Screenshot 2023-11-15 at 19 08 07" src="https://github.com/thomasdevl/HackaPython/assets/91684310/3ce6fb65-2959-4abb-91a0-6b0a099322b4">

### first_piece_x, first_piece_y
<img width="448" alt="Screenshot 2023-11-15 at 19 08 26" src="https://github.com/thomasdevl/HackaPython/assets/91684310/2967e5e6-5fe6-4d0f-8ab4-868823c86860">

### next_piece_x, next_piece_y
<img width="354" alt="Screenshot 2023-11-15 at 19 09 44" src="https://github.com/thomasdevl/HackaPython/assets/91684310/adcfd410-9953-424c-9073-5aa89110dc02">

### accept_x, accept_y
<img width="684" alt="Screenshot 2023-11-15 at 19 10 07" src="https://github.com/thomasdevl/HackaPython/assets/91684310/479f35af-78af-418d-a4e1-13f6055541c2">

### game_over_x, game_over_y 
<img width="785" alt="Screenshot 2023-11-15 at 19 12 32" src="https://github.com/thomasdevl/HackaPython/assets/91684310/ade9b092-317b-402c-bc32-91349852c030">

2. Run the following command in the terminal:

```bash
python3 main.py
```

2*. if you get an error related to the self.color_to_piece dictionnary then you need to update the color values in the config.py.
