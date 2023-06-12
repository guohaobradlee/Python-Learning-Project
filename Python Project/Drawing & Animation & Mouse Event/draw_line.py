"""
File: draw_line.py
Name:Brad Lee
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# The diameter of point.
SIZE = 10


window = GWindow(title='draw_line.py')
# The start point.
dot = GOval(SIZE, SIZE)
# Use first_x and first_y to record the position coordinate of start point.
first_x = 0
first_y = 0
# Check if there are two points.
two_point = False


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global first_x
    global first_y
    global two_point
    if not two_point:
        window.add(dot, mouse.x - SIZE / 2, mouse.y - SIZE / 2)
        first_x = mouse.x
        first_y = mouse.y
        two_point = True
    else:
        line = GLine(first_x, first_y, mouse.x, mouse.y)
        first_x = 0
        first_y = 0
        two_point = False
        window.add(line)
        window.remove(dot)


if __name__ == "__main__":
    main()
