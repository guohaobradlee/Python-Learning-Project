"""
File: my_drawing.py
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    User use campy module to
    draw their own picture.
    """
    window = GWindow(800, 800, title='Find My.app')
    frame_one = GRect(500, 450, x=150, y=175)
    frame_two = GRect(450, 500, x=175, y=150)
    corner_one = GOval(50, 50, x=150, y=150)
    corner_two = GOval(50, 50, x=150, y=600)
    corner_three = GOval(50, 50, x=600, y=150)
    corner_four = GOval(50, 50, x=600, y=600)
    outer = GOval(400, 400, x=200, y=200)
    middle_circle = GOval(250, 250, x=275, y=275)
    middle = GOval(240, 240, x=280, y=280)
    central_circle = GOval(70, 70, x=365, y=365)
    central = GOval(50, 50, x=375, y=375)
    left_radar_line = GLine(400, 400, 258.42, 258.58)
    right_radar_line = GLine(400, 400, 541.42, 258.58)
    stancode_point = GOval(20, 20, x=400, y=300)
    jerry_point = GOval(20, 20, x=335, y=515)
    stanford_point = GOval(20, 20, x=240, y=330)
    sc101_point = GOval(20, 20, x=500, y=500)
    sc001_point = GOval(20, 20, x=475, y=260)
    stancode_label = GLabel('Mom', x=380, y=300)
    jerry_label = GLabel('Dad', x=330, y=515)
    stanford_label = GLabel('iPhone', x=225, y=330)
    sc101_label = GLabel('MacBook', x=490, y=500)
    sc001_label = GLabel('iPad', x=465, y=260)
    find_my_label = GLabel('Find My', x=300, y=720)
    window.add(frame_one)
    frame_one.color = 'gainsboro'
    frame_one.filled = True
    frame_one.fill_color = 'gainsboro'
    window.add(frame_two)
    frame_two.color = 'gainsboro'
    frame_two.filled = True
    frame_two.fill_color = 'gainsboro'
    window.add(corner_one)
    corner_one.color = 'gainsboro'
    corner_one.filled = True
    corner_one.fill_color = 'gainsboro'
    window.add(corner_two)
    corner_two.color = 'gainsboro'
    corner_two.filled = True
    corner_two.fill_color = 'gainsboro'
    window.add(corner_three)
    corner_three.color = 'gainsboro'
    corner_three.filled = True
    corner_three.fill_color = 'gainsboro'
    window.add(corner_four)
    corner_four.color = 'gainsboro'
    corner_four.filled = True
    corner_four.fill_color = 'gainsboro'
    window.add(outer)
    outer.color = 'springgreen'
    outer.filled = True
    outer.fill_color = 'springgreen'
    window.add(middle_circle)
    middle_circle.color = 'snow'
    middle_circle.filled = True
    middle_circle.fill_color = 'snow'
    window.add(middle)
    middle.color = 'mediumspringgreen'
    middle.filled = True
    middle.fill_color = 'mediumspringgreen'
    window.add(central_circle)
    central_circle.color = 'white'
    central_circle.filled = True
    central_circle.fill_color = 'white'
    window.add(central)
    central.color = 'royalblue'
    central.filled = True
    central.fill_color = 'royalblue'
    window.add(left_radar_line)
    left_radar_line.color = 'royalblue'
    window.add(right_radar_line)
    right_radar_line.color = 'royalblue'
    window.add(stancode_point)
    stancode_point.color = 'crimson'
    stancode_point.filled = True
    stancode_point.fill_color = 'crimson'
    window.add(jerry_point)
    jerry_point.color = 'crimson'
    jerry_point.filled = True
    jerry_point.fill_color = 'crimson'
    window.add(stanford_point)
    stanford_point.color = 'crimson'
    stanford_point.filled = True
    stanford_point.fill_color = 'crimson'
    window.add(sc101_point)
    sc101_point.color = 'crimson'
    sc101_point.filled = True
    sc101_point.fill_color = 'crimson'
    window.add(sc001_point)
    sc001_point.color = 'crimson'
    sc001_point.filled = True
    sc001_point.fill_color = 'crimson'
    window.add(stancode_label)
    window.add(jerry_label)
    window.add(stanford_label)
    window.add(sc101_label)
    window.add(sc001_label)
    window.add(find_my_label)
    find_my_label.font = '-60'


if __name__ == '__main__':
    main()
