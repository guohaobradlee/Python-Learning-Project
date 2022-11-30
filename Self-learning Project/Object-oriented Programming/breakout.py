"""
Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman.
"""


from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    while True:
        if graphics.start_or_not is True:
            graphics.check_for_collision()
            graphics.reset_ball()
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.lives_left == 0:
            break
        if graphics.numbers_of_brick == 0:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()