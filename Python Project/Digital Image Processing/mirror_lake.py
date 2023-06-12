"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""


from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image.
    :return: img: a mirrored image of the original image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    reflected_image = SimpleImage.blank(original_mt.width, original_mt.height * 2)
    for y in range(original_mt.height):
        for x in range(original_mt.width):
            original_mt_pixel = original_mt.get_pixel(x, y)
            reflected_upper = reflected_image.get_pixel(x, y)
            reflected_lower = reflected_image.get_pixel(x, reflected_image.height-y-1)
            # Fill the upper empty pixel.
            reflected_upper.red = original_mt_pixel.red
            reflected_upper.green = original_mt_pixel.green
            reflected_upper.blue = original_mt_pixel.blue
            # Fill the lower empty pixel
            reflected_lower.red = original_mt_pixel.red
            reflected_lower.green = original_mt_pixel.green
            reflected_lower.blue = original_mt_pixel.blue
    return reflected_image


def main():
    """
    Users can input a image in this function, and will get a mirrored image of the original image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
