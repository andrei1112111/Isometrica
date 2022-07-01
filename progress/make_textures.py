from dataclasses import dataclass

import pygame.image

# init
pathB = "GameData/textures/block"


@dataclass
class Textures:
    grass: pygame.image.load(pathB + "grass").convert()
