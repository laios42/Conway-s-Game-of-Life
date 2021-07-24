# *Conway's Game of Life*

The game of life is a cellular automaton imagined by John H. Conway in the 1970s and is probably, the best known of all cellular automata. Despite very simple rules, the game of life is Turing-complete and deterministic.

<img src="conways_gol_rec.gif"/>

**The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.**

The game is a grid of cells, each of which can be in either of the two states, alive or dead. There are some rules which alter the state of the cells. At each stage, the evolution of a cell is entirely determined by its current state and the state of its eight neighbours.

The game only has 4 simple rules:
1. Any live cell with fewer than two live neighbours dies, as if by under population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

