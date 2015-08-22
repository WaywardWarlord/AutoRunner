import random

def __init__():

    global player_jump_height
    global BLACK
    global WHITE
    global GREEN
    global RED
    global BLUE
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    #global platform_width
    #global platform_height
    #global platform_x
    #global platform_y
    global player_width
    global player_height
    global player_jump_length
    global player_jump_height

    # Global constants
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    BLUE = (0,0,255)

    # Screen constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600


    # Global vars
    player_height = 60
    player_width = 40
    player_jump_height = -10
    player_jump_length = 90
    player_pos = (340, SCREEN_HEIGHT - 60 - 100)
    #platform_width = random.randrange(SCREEN_WIDTH - 200, SCREEN_WIDTH + 400)
    #platform_height = SCREEN_HEIGHT - 200
    #platform_x = random.randrange(platform_width + player_width, platform_width + player_jump_length)
    #platform_y = random.randrange(platform_height, platform_height + 100)
