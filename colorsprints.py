# Some ANSI escape sequences for colours and effects
import colorama

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color(text :str,*color :str)-> None:
    """change colors of the texts

    Args:
        text (str): text to be colored
        color (str): tells the color
    """
    effects="".join(color)
    print("{}{}{}".format(effects,text,RESET))

colorama.init()
color("VLALLVLMSOAUMC",BLUE, BOLD)
color("VLALLVLMSOAUMC",RED, UNDERLINE)
color("VLALLVLMSOAUMC",MAGENTA, BOLD)
color("VLALLVLMSOAUMC",GREEN, REVERSE)
#color(YELLOW,"VLALLVLMSOAUMC")
#color(CYAN,"VLALLVLMSOAUMC")
#color(BOLD,"VLALLVLMSOAUMC")
#color(UNDERLINE,"VLALLVLMSOAUMC")
#color(REVERSE,"VLALLVLMSOAUMC")
colorama.deinit()