import pygame
import os
from game_folder.game import Game
import 
pygame.init()



SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
window_size = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)


screen = pygame.display.set_mode((window_size))
clock = pygame.time.Clock()
pygame.display.set_caption('Informatica game')


print(os.getcwd())
pygame.display.toggle_fullscreen()


game = Game(screen, clock, window_size)
game.run()




pygame.quit()