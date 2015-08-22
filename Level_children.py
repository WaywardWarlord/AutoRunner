import pygame
import Global_vars
from Level_mother import Level
from Platform import Platform
import random
from Functions import adding

class Level_01(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with the width, height, x, and y of platform

        platforms = 4
        width = []
        width.append(random.randrange(Global_vars.SCREEN_WIDTH - 200, Global_vars.SCREEN_WIDTH + 400))
        height = Global_vars.SCREEN_HEIGHT - 200
        platform_level = [[width[0], height, 0, 450]]
        i = 0

        while platforms > 0:
            if platforms > 0:
                width.append(random.randrange(Global_vars.SCREEN_WIDTH - 200, Global_vars.SCREEN_WIDTH + 400))
                gap = random.randrange(120, Global_vars.player_jump_length)
                if len(width) > 2:
                    x += width[i] + gap
                else:
                    x = width[i] + gap
                y = random.randrange(height, height + 50)
                if x <= width[i]:
                    x += Global_vars.player_jump_length
                platform_level.append([width[-1], height, x, y])
                platforms -= 1
                i += 1

        # Go through the array above and add playforms
        for platform in platform_level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
