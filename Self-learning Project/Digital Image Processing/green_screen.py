"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""


from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image.
    :param figure_img: SimpleImage, green screen figure image.
    :return: figure_img: SimpleImage, the green screen pixels are replaced by pixels background image.
    """
    background_img.make_as_big_as(figure_img)
    for y in range(background_img.height):
        for x in range(background_img.width):
            figure_img_pixel = figure_img.get_pixel(x, y)
            background_img_pixel = background_img.get_pixel(x, y)
            bigger = max(figure_img_pixel.red, figure_img_pixel.blue)  # Return the one that is bigger.
            if figure_img_pixel.green > bigger * 2:
                figure_img_pixel.red = background_img_pixel.red
                figure_img_pixel.green = background_img_pixel.green
                figure_img_pixel.blue = background_img_pixel.blue
    return figure_img


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop a person onto any background.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
