import pygame
import Global_vars

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height):

        super().__init__()

        self.width = width
        self.height = height

        self.image = pygame.Surface([width, height])
        self.image.fill(Global_vars.GREEN)

        self.rect = self.image.get_rect()
