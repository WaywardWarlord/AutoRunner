import pygame
import Global_vars

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # How far the world should be scrolled left/right
        self.world_shift = 0

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):

        # Draw the background
        screen.fill(Global_vars.BLUE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ Scroll the screen."""

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
