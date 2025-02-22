import pygame
import Maze
from pygame.locals import *
import asyncio
import lock as lk
import Game
import time

async def main():
    pygame.init()
    win=pygame.display.set_mode((1920, 1080))

    ##TODO load resources
    mainMenu = pygame.image.load("main.png")
    winningScreen = pygame.image.load("winscreen.png")
    losingScreen = pygame.image.load("losescreen.png")

    ## TODO get coordinates of buttons
    startButton = pygame.Rect(x1, y1, x2, y2)
    exitButton  = pygame.Rect(x1, y1, x2, y2)

    clock = pygame.time.Clock()

    run = True
    hasPlayed = False

    display = mainMenu

    while run:
        win.blit(display,(0, 0))

        if hasPlayed:
            time.sleep(5)
            display = mainMenu
            hasPlayed = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()             # Location of the mouse-click

                if (exitButton.collidepoint(mouse_position)):    
                    run = False
                    pygame.quit()
                    break

                if (startButton.collidepoint(mouse_position)):    
                    game = Game.Game(win)
                    if (game.run()):
                        display = winningScreen
                    else:
                        display = losingScreen
                    hasPlayed = True

            if event.type == QUIT:
                run = False
                pygame.quit()
                break

        pygame.display.flip()    
        clock.tick(60)

    return

asyncio.run(main())
