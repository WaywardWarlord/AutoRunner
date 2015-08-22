import pygame
import Global_vars
from Level_mother import Level
from Platform import Platform
import random

class Level_01(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with the width, height, x, and y of platform
        #level = [[Global_vars.platform_width, Global_vars.platform_height, 300, 540],
        #         [Global_vars.platform_width, Global_vars.platform_height, Global_vars.platform_x, Global_vars.platform_y]
        #         ]

        #platform_width = random.randrange(SCREEN_WIDTH - 200, SCREEN_WIDTH + 400)
        #platform_height = SCREEN_HEIGHT - 200
        #platform_x = random.randrange(platform_width + player_width, platform_width + player_jump_length)
        #platform_y = random.randrange(platform_height, platform_height + 100)

        platforms = 5
        old_width = 0
        platform_level = []

        while platforms > 0:
            if platforms > 0:
                width = random.randrange(Global_vars.SCREEN_WIDTH - 200, Global_vars.SCREEN_WIDTH + 400)
                height = Global_vars.SCREEN_HEIGHT - 200
                if platforms == 5:
                    x = width + random.randrange(Global_vars.player_width, Global_vars.player_jump_length)
                    y = random.randrange(height, height + 100)
                else:
                    x = old_width + random.randrange(Global_vars.player_width, Global_vars.player_jump_length)
                    y = random.randrange(height, height + 100)
                if x <= width:
                    x += Global_vars.player_jump_length
                platform_level.append([width, height, x, y])
                platforms -= 1
                old_width = width
                print (width)
                print (height )
                print (x)
                print (y)
        print (platform_level)

        # Go through the array above and add playforms
        for platform in platform_level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
