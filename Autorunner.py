""" Autorunning game """
import pygame
import random

# Global vars
player_jump_height = -10

# Global constants
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

# Screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):

    def __init__(self):

        # Calls the pygame Sprite
        super().__init__()

        # Image of Player
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # Set a rectangle hitbox
        self.rect = self.image.get_rect()

        # Set speed vector of Player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bumb against
        self.level = None

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

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # Check if we are on the ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because if doesn't work well if we only move down 1
        # when working with a platform moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set out speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = player_jump_height


    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

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
        screen.fill(BLUE)

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

class Level_01(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with the width, height, x, and y of platform
        #platform_x = random.randrange(player_jump_height)
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]

        # Go through the array above and add playforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

def main():
    """ Main Program """
    pygame.init()

    # Set height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("AutoRunner")

    # Create the Player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # --- Main Program Loop ---
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the Player
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player goes near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # All code to draw is below this comment!!!
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # Limit to 60 frames per second
        clock.tick(60)

        # Update the screen with what we've drawn
        pygame.display.flip()

    # Be IDLE friendly. If not, the program will 'hang' on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
