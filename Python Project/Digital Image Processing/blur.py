"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""


from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, an original image.
    :return: img: SimpleImage, image with blurred effect.
    """
    blank_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            blurred = blank_img.get_pixel(x, y)
            if x == 0 and y == 0:
                """
                For 4 corners.
                The  new RGB values of original pixel is the average RGB values
                of the original pixel and the other pixels around it.
                """
                avg_red1 = (img.get_pixel(x, y).red +
                            img.get_pixel(x + 1, y).red +
                            img.get_pixel(x, y + 1).red +
                            img.get_pixel(x + 1, y + 1).red) / 4
                avg_green1 = (img.get_pixel(x, y).green +
                              img.get_pixel(x + 1, y).green +
                              img.get_pixel(x, y + 1).green +
                              img.get_pixel(x + 1, y + 1).green) / 4
                avg_blue1 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x + 1, y).blue +
                             img.get_pixel(x, y + 1).blue +
                             img.get_pixel(x + 1, y + 1).blue) / 4
                blurred.red = avg_red1
                blurred.green = avg_green1
                blurred.blue = avg_blue1
            elif x == 0 and y == blank_img.height - 1:
                avg_red2 = (img.get_pixel(x, y).red +
                            img.get_pixel(x, y - 1).red +
                            img.get_pixel(x + 1, y - 1).red +
                            img.get_pixel(x + 1, y).red) / 4
                avg_green2 = (img.get_pixel(x, y).green +
                              img.get_pixel(x, y - 1).green +
                              img.get_pixel(x + 1, y - 1).green +
                              img.get_pixel(x + 1, y).green) / 4
                avg_blue2 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x, y - 1).blue +
                             img.get_pixel(x + 1, y - 1).blue +
                             img.get_pixel(x + 1, y).blue) / 4
                blurred.red = avg_red2
                blurred.green = avg_green2
                blurred.blue = avg_blue2
            elif x == blank_img.width - 1 and y == 0:
                avg_red3 = (img.get_pixel(x, y).red +
                            img.get_pixel(x - 1, y).red +
                            img.get_pixel(x - 1, y + 1).red +
                            img.get_pixel(x, y + 1).red) / 4
                avg_green3 = (img.get_pixel(x, y).green +
                              img.get_pixel(x - 1, y).green +
                              img.get_pixel(x - 1, y + 1).green +
                              img.get_pixel(x, y + 1).green) / 4
                avg_blue3 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x - 1, y).blue +
                             img.get_pixel(x - 1, y + 1).blue +
                             img.get_pixel(x, y + 1).blue) / 4
                blurred.red = avg_red3
                blurred.green = avg_green3
                blurred.blue = avg_blue3
            elif x == blank_img.width - 1 and y == blank_img.height - 1:
                avg_red4 = (img.get_pixel(x, y).red +
                            img.get_pixel(x, y - 1).red +
                            img.get_pixel(x - 1, y - 1).red +
                            img.get_pixel(x - 1, y).red) / 4
                avg_green4 = (img.get_pixel(x, y).green +
                              img.get_pixel(x, y - 1).green +
                              img.get_pixel(x - 1, y - 1).green +
                              img.get_pixel(x - 1, y).green) / 4
                avg_blue4 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x, y - 1).blue +
                             img.get_pixel(x - 1, y - 1).blue +
                             img.get_pixel(x - 1, y).blue) / 4
                blurred.red = avg_red4
                blurred.green = avg_green4
                blurred.blue = avg_blue4
            elif x == 0 and 0 < y < blank_img.height - 1:
                """
                For 4 edges.
                The  new RGB values of original pixel is the average RGB values 
                of the original pixel and the other pixels around it.
                """
                avg_red5 = (img.get_pixel(x, y).red +
                            img.get_pixel(x, y - 1).red +
                            img.get_pixel(x + 1, y - 1).red +
                            img.get_pixel(x + 1, y).red +
                            img.get_pixel(x + 1, y + 1).red +
                            img.get_pixel(x, y + 1).red) / 6
                avg_green5 = (img.get_pixel(x, y).green +
                              img.get_pixel(x, y - 1).green +
                              img.get_pixel(x + 1, y - 1).green +
                              img.get_pixel(x + 1, y).green +
                              img.get_pixel(x + 1, y + 1).green +
                              img.get_pixel(x, y + 1).green) / 6
                avg_blue5 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x, y - 1).blue +
                             img.get_pixel(x + 1, y - 1).blue +
                             img.get_pixel(x + 1, y).blue +
                             img.get_pixel(x + 1, y + 1).blue +
                             img.get_pixel(x, y + 1).blue) / 6
                blurred.red = avg_red5
                blurred.green = avg_green5
                blurred.blue = avg_blue5
            elif x == blank_img.width - 1 and 0 < y < blank_img.height - 1:
                avg_red6 = (img.get_pixel(x, y).red +
                            img.get_pixel(x, y - 1).red +
                            img.get_pixel(x - 1, y - 1).red +
                            img.get_pixel(x - 1, y).red +
                            img.get_pixel(x - 1, y + 1).red +
                            img.get_pixel(x, y + 1).red) / 6
                avg_green6 = (img.get_pixel(x, y).green +
                              img.get_pixel(x, y - 1).green +
                              img.get_pixel(x - 1, y - 1).green +
                              img.get_pixel(x - 1, y).green +
                              img.get_pixel(x - 1, y + 1).green +
                              img.get_pixel(x, y + 1).green) / 6
                avg_blue6 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x, y - 1).blue +
                             img.get_pixel(x - 1, y - 1).blue +
                             img.get_pixel(x - 1, y).blue +
                             img.get_pixel(x - 1, y + 1).blue +
                             img.get_pixel(x, y + 1).blue) / 6
                blurred.red = avg_red6
                blurred.green = avg_green6
                blurred.blue = avg_blue6
            elif y == 0 and 0 < x < blank_img.width - 1:
                avg_red7 = (img.get_pixel(x, y).red +
                            img.get_pixel(x - 1, y).red +
                            img.get_pixel(x - 1, y + 1).red +
                            img.get_pixel(x, y + 1).red +
                            img.get_pixel(x + 1, y + 1).red +
                            img.get_pixel(x + 1, y).red) / 6
                avg_green7 = (img.get_pixel(x, y).green +
                              img.get_pixel(x - 1, y).green +
                              img.get_pixel(x - 1, y + 1).green +
                              img.get_pixel(x, y + 1).green +
                              img.get_pixel(x + 1, y + 1).green +
                              img.get_pixel(x + 1, y).green) / 6
                avg_blue7 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x - 1, y).blue +
                             img.get_pixel(x - 1, y + 1).blue +
                             img.get_pixel(x, y + 1).blue +
                             img.get_pixel(x + 1, y + 1).blue +
                             img.get_pixel(x + 1, y).blue) / 6
                blurred.red = avg_red7
                blurred.green = avg_green7
                blurred.blue = avg_blue7
            elif y == blank_img.height - 1 and 0 < x < blank_img.width - 1:
                avg_red8 = (img.get_pixel(x, y).red +
                            img.get_pixel(x - 1, y).red +
                            img.get_pixel(x - 1, y - 1).red +
                            img.get_pixel(x, y - 1).red +
                            img.get_pixel(x + 1, y - 1).red +
                            img.get_pixel(x + 1, y).red) / 6
                avg_green8 = (img.get_pixel(x, y).green +
                              img.get_pixel(x - 1, y).green +
                              img.get_pixel(x - 1, y - 1).green +
                              img.get_pixel(x, y - 1).green +
                              img.get_pixel(x + 1, y - 1).green +
                              img.get_pixel(x + 1, y).green) / 6
                avg_blue8 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x - 1, y).blue +
                             img.get_pixel(x - 1, y - 1).blue +
                             img.get_pixel(x, y - 1).blue +
                             img.get_pixel(x + 1, y - 1).blue +
                             img.get_pixel(x + 1, y).blue) / 6
                blurred.red = avg_red8
                blurred.green = avg_green8
                blurred.blue = avg_blue8
            else:
                """
                For other area except the corners and edges.
                The  new RGB values of original pixel is the average RGB values 
                of the other pixels around it.
                """
                avg_red9 = (img.get_pixel(x, y).red +
                            img.get_pixel(x - 1, y).red +
                            img.get_pixel(x + 1, y).red +
                            img.get_pixel(x - 1, y - 1).red +
                            img.get_pixel(x, y - 1).red +
                            img.get_pixel(x + 1, y - 1).red +
                            img.get_pixel(x - 1, y + 1).red +
                            img.get_pixel(x, y + 1).red +
                            img.get_pixel(x + 1, y + 1).red) / 9
                avg_green9 = (img.get_pixel(x, y).green +
                              img.get_pixel(x - 1, y).green +
                              img.get_pixel(x + 1, y).green +
                              img.get_pixel(x - 1, y - 1).green +
                              img.get_pixel(x, y - 1).green +
                              img.get_pixel(x + 1, y - 1).green +
                              img.get_pixel(x - 1, y + 1).green +
                              img.get_pixel(x, y + 1).green +
                              img.get_pixel(x + 1, y + 1).red) / 9
                avg_blue9 = (img.get_pixel(x, y).blue +
                             img.get_pixel(x - 1, y).blue +
                             img.get_pixel(x + 1, y).blue +
                             img.get_pixel(x - 1, y - 1).blue +
                             img.get_pixel(x, y - 1).blue +
                             img.get_pixel(x + 1, y - 1).blue +
                             img.get_pixel(x - 1, y + 1).blue +
                             img.get_pixel(x, y + 1).blue +
                             img.get_pixel(x + 1, y + 1).blue) / 9
                blurred.red = avg_red9
                blurred.green = avg_green9
                blurred.blue = avg_blue9
    return blank_img


def main():
    """
    Users can use this program to make an image blur,
    and users can change the number in for loop to adjust the degree of blur.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(50):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
