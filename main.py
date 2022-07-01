import pygame
from configparser import ConfigParser
from pygame.locals import SCALED, DOUBLEBUF

# init
pygame.init()
pygame.mixer.init()

config = ConfigParser()
config.read('config.ini')

screen = pygame.display.set_mode((
    int(config['window']['width']),
    int(config['window']['height'])
), SCALED | DOUBLEBUF)
pygame.display.set_caption(config['window']['title'])
clock = pygame.time.Clock()

running = True

# main loop
while running:
    clock.tick(int(config['game']['fps']))
    screen.fill((int(config['game']['background']),) * 3)

    pygame.display.flip()

pygame.quit()
