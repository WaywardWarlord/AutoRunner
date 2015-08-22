import pygame
import random
import Global_vars

class Player(pygame.sprite.Sprite):

    def __init__(self):

        # Calls the pygame Sprite
        super().__init__()

        # Image of Player
        width = Global_vars.player_width
        height = Global_vars.player_height
        self.image = pygame.Surface([width, height])
        self.image.fill(Global_vars.RED)

        # Set a rectangle hitbox
        self.rect = self.image.get_rect()

        # Set speed vector of Player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bumb against
        self.level = None

        self.starting_position = Global_vars.SCREEN_HEIGHT - self.rect.height - 100

    def update(self):

        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if the Player hits anything
        block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
        for block in block_hit_list:
            # If the player is moving right
            # set out right side to the left side of the item we hits
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the oppositee
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check to see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset the plyer's position based on the top\bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

                # Stop our vertical movement
                self.change_y = 0

        # Player pos
        Global_vars.player_pos = (self.rect.x, self.rect.y)

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # Check if we are on the ground
        if self.rect.y >= Global_vars.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = Global_vars.SCREEN_HEIGHT - self.rect.height

    def jump(self):

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because if doesn't work well if we only move down 1
        # when working with a platform moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set out speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= Global_vars.SCREEN_HEIGHT:
            self.change_y = Global_vars.player_jump_height


    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0
