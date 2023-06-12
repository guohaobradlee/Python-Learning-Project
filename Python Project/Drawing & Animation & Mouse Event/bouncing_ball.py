"""
File: 
Name:
-------------------------
TODO:
"""


from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


# Constants.
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


# Global variables.
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
times = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(start_drop)


def start_drop(mouse):
    global times
    vy = 0
    while True:
        onmouseclicked(no_function)
        # if the ball is out of the window 3 times, this program will be terminated.
        if times == 0:
            break
        ball.move(VX, vy)
        vy += GRAVITY
        # For bounce back.
        if ball.y + ball.height > window.height:
            vy = -vy * REDUCE
        # If the ball is out of the window, it will appear at the original position.
        elif ball.x > window.width:
            times -= 1
            window.remove(ball)
            break
        pause(DELAY)
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(start_drop)


# Eliminate mouse clicked interference during the process of bouncing.
def no_function(mouse):
    pass


if __name__ == "__main__":
    main()
