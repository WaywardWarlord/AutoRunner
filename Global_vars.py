import time
def __init__():

    global player_jump_height
    global BLACK
    global WHITE
    global GREEN
    global RED
    global BLUE
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global player_width
    global player_height
    global player_jump_length
    global player_jump_height
    global steps
    global platforms
    global player_speed


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
    player_jump_length = 170
    player_pos = (340, SCREEN_HEIGHT)
    steps = 0
    platforms = 0
    player_speed = 8.0
