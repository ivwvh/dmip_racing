# ANSI цвета
BLACK = u'\033[0;30m'
RED = u'\033[0;31m'
GREEN = u'\033[0;32m'
BROWN = u'\033[0;33m'
BLUE = u'\033[0;34m'
PURPLE = u'\033[0;35m'
CYAN = u'\033[0;36m'
LIGHT_GRAY = u'\033[0;37m'
DARK_GRAY = u'\033[1;30m'
LIGHT_RED = u'\033[1;31m'
LIGHT_GREEN = u'\033[1;32m'
YELLOW = u'\033[1;33m'
LIGHT_BLUE = u'\033[1;34m'
LIGHT_PURPLE = u'\033[1;35m'
LIGHT_CYAN = u'\033[1;36m'
LIGHT_WHITE = u'\033[1;37m'
END_COLOR = u'\033[0m'

WALL = DARK_GRAY + '┇' + END_COLOR
PLAYER_IMAGE = GREEN + 'P' + END_COLOR
OBSTACLE_IMAGE = YELLOW + 'O' + END_COLOR
CELL_IMAGE = LIGHT_GRAY + '.' + END_COLOR


FPS = 10
KEYS = {
    'up': 'up',
    'down': 'down',
    'left': 'left',
    'right': 'right',
    'exit': 'esc',
}

'''TODO: images for objs'''