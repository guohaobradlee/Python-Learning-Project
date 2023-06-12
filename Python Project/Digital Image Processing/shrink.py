"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""


from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image.
    :return img: SimpleImage, a quarter size og the original image.
    """
    original = SimpleImage(filename)
    # Make a quarter size blank image of the original image.
    shrink_img = original.blank(original.width // 2, original.height // 2)
    for y in range(original.height):
        for x in range(original.width):
            # Get 4 pixels each times in original image.
            if x * 2 < original.width and y * 2 < original.height:
                # Get pixels in shrunk image.
                shrink_img_pixel = shrink_img.get_pixel(x, y)
                # Put average RGB values of 4 pixels each times into one pixel of shrunk image.
                quarter_red = (original.get_pixel(x * 2, y * 2).red +
                               original.get_pixel(x * 2 + 1, y * 2).red +
                               original.get_pixel(x * 2, y * 2 + 1).red +
                               original.get_pixel(x * 2 + 1, y * 2 + 1).red) / 4
                quarter_green = (original.get_pixel(x * 2, y * 2).green +
                                 original.get_pixel(x * 2 + 1, y * 2).green +
                                 original.get_pixel(x * 2, y * 2 + 1).green +
                                 original.get_pixel(x * 2 + 1, y * 2 + 1).green) / 4
                quarter_blue = (original.get_pixel(x * 2, y * 2).blue +
                                original.get_pixel(x * 2 + 1, y * 2).blue +
                                original.get_pixel(x * 2, y * 2 + 1).blue +
                                original.get_pixel(x * 2 + 1, y * 2 + 1).blue) / 4
                shrink_img_pixel.red = quarter_red
                shrink_img_pixel.green = quarter_green
                shrink_img_pixel.blue = quarter_blue
    return shrink_img


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
