""" Autorunning game """
import pygame
import random
from Player import Player
import Global_vars
from Platform import Platform
from Level_mother import Level
from Level_children import Level_01, Level_02

Global_vars.__init__()

def main():
    """ Main Program """
    pygame.init()

    # Set height and width of the screen
    size = [Global_vars.SCREEN_WIDTH, Global_vars.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("AutoRunner")

    # Create the Player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))

    # Set current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 140
    player.rect.y = player.starting_position
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
                if event.key == pygame.K_UP:
                    player.jump()


        if Global_vars.steps == Global_vars.tick:
            Global_vars.platforms += 1
            Global_vars.tick += 1

        # Update the Player
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player goes near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 140
            player.rect.y = Global_vars.SCREEN_HEIGHT / 2
            if current_level_no < len(level_list) -1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # Makes the player Autorun
        player.go_right()

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
