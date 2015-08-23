import pygame
import Global_vars

def make_platforms():
    i = 0
    while Global_vars.platforms > 0:
        if Global_vars.platforms > 0:
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
            Global_vars.platforms -= 1
            i += 1
