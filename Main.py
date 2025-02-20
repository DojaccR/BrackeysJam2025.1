import pygame
import Maze
from pygame.locals import *
import asyncio
import lock as lk

async def main():
    pygame.init()
    win=pygame.display.set_mode((1920, 1080))

    ##TODO load resources
    mainMenu = pygame.image.load("main.png")

    run = True

    display = mainMenu

    while run:
        ##TODO display current screen
        win.blit(display,(0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                ##TODO On exit
                run = False
                pygame.quit()

                ##TODO On start
                    ## instantiate game
                        ## if run false
                            ## display losing screen
                        ## if run true
                            ## display winning screen

                    ## display main menu

        pass

