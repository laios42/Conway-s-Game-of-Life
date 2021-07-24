import pygame
import numpy as np
import os
import grid

# to center the window
os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 1200, 700
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)

# to control the frame rate
clock = pygame.time.Clock()
fps = 28

# colors in RGB notation
black = (0, 0, 0)
white = (255, 255, 255)

px_scale = 15     # size of pixels
offset = 2      # offset between pixels

Grid = grid.Grid(width, height, px_scale, offset)   # creating the grid
Grid.random2d_array()   # initializing grid with random cell values (either alive or dead)

pause = False
run = True

while run:

    clock.tick(fps)

    # controls when an input is provided
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
    
    Grid.Conway(off_color=black, on_color=white, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    # to update the grid and play as an animation
    pygame.display.update()

pygame.quit()
