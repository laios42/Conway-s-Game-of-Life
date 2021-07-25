# *Conway's Game of Life*

The game was devised by John Conway in 1970 as a way to explain unpredictable cellular automaton. Despite very simple rules, the game of life is Turing-complete and deterministic.

<p align="center"><img src="conways_gol_rec.gif" alt="Simulation" style="width:100%;"><p align="center">Simulation.</p></p>

**The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.**

The game is a grid of cells, each of which can be in either of the two states, alive or dead. There are some rules which alter the state of the cells. At each stage, the evolution of a cell is entirely determined by its current state and the state of its eight neighbours.

The game only has 4 simple rules:
1. Any live cell with fewer than two live neighbours dies, as if by under population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

It is interesting to see that such complex systems can emerge from such elementary rules and configurations — It kind of reminds us of the real world, where elementary blocks congregate to generate much more complex structures such as life.

## To Run Simulation
   navigate to the directory that contains main.py and execute main.py:
       
       python main.py

### Requirements
   pygame :
   
        pip install pygame
   numpy :
   
        pip install numpy
       
### Controls
       * "spacebar" to pause simulation
       * "left mouse click" to insert a live cell
       * "esc" to exit
