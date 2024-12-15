#################################################################
# FILE: image_editor.py
# WRITER: Shai Feldman, shai.feldman@huji.ac.il , 332519636
# EXERCISE: intro2cs ex6 2025
##############################################################################
#                                   Imports                                  #
##############################################################################
import sys
from math import floor

import PIL

from ex6_helper import *

##############################################################################
#                                  Functions                                 #
##############################################################################

EXAMPLE_IMAGE = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                 [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                 [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                 [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]


def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """
    Separates an image to a list of single-channel images.
    :param image: image to separate
    :return: a list of channels as
    """
    num_of_channels = len(image[0][0])
    separate_channels_list = [[] for _ in range(num_of_channels)]
    for original_row in image:
        for i in range(num_of_channels):
            separate_channels_list[i].append([pixel[i] for pixel in original_row])
    return separate_channels_list


def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    """
    Combines a list of single-channel images into a combined image.
    :param channels: list of single-channel images
    :return: combined image
    """
    combined_image = []
    for row_idx in range(len(channels[0])):
        combined_row = []
        for col_idx in range(len(channels[0][0])):
            pixel = [channels[channel_idx][row_idx][col_idx] for channel_idx in range(len(channels))]
            combined_row.append(pixel)
        combined_image.append(combined_row)
    return combined_image


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """
    Converts an RGB image to grayscale.
    :param colored_image: image to convert to grayscale
    :return: grayscale image
    """
    grayscale_image = []
    pixels_to_grayscale = lambda x: round(x[0] * 0.299 + x[1] * 0.587 + x[2] * 0.114)
    for row in colored_image:
        grayscale_image.append([pixels_to_grayscale(pixel) for pixel in row])
    return grayscale_image


def blur_kernel(size: int) -> Kernel:
    """
    Creates a blur kernel of a specific size.
    :param size: kernel size
    :return: blur kernel
    """
    return [[1 / size ** 2 for _ in range(size)] for _ in range(size)]


def create_sub_matrix(image: SingleChannelImage,
                      pixel: tuple[int, int],
                      size: int) -> SingleChannelImage:
    """
    Creates a submatrix of an image with the given size.
    Used to apply kernel to a specific pixel.
    :param image: original image
    :param pixel: center pixel of the new submatrix
    :param size: size of the new submatrix
    :return:
    """
    sub_image = []
    row_index = pixel[0] - (size // 2)
    for i in range(size):
        new_row = []
        col_index = pixel[1] - (size // 2)
        for _ in range(size):
            if row_index < 0 or col_index < 0 or row_index > len(image) - 1 or col_index > len(image[0]) - 1:
                new_row.append(image[pixel[0]][pixel[1]])
            else:
                new_row.append(image[row_index][col_index])
            col_index += 1
        sub_image.append(new_row)
        row_index += 1
    return sub_image


def multiply_with_kernel(sub_image: SingleChannelImage, kernel: Kernel) -> int:
    """
    Multiplies a submatrix of an image with a kernel.
    :param sub_image: image
    :param kernel: kernel to multiply
    :return: the sum of the multiplied matrices
    """
    value = 0
    for row in range(len(sub_image)):
        for col in range(len(sub_image[0])):
            value += sub_image[row][col] * kernel[row][col]
    if value < 0:
        return 0
    if value > 255:
        return 255
    return round(value)


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """
    Applies a kernel to an image.
    :param image: original image
    :param kernel: kernel to apply
    :return: image blured by kernel
    """
    blurred_image = []
    for row in range(len(image)):
        new_row = []
        for col in range(len(image[0])):
            sub_image = create_sub_matrix(image, (row, col), len(kernel))
            new_row.append(multiply_with_kernel(sub_image, kernel))
        blurred_image.append(new_row)
    return blurred_image


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    """
    Performs bilinear interpolation on an image.
    :param image: original image
    :param y: y coordinate of the point
    :param x: x coordinate of the point
    :return: interpolated value
    """
    rows, cols = len(image), len(image[0])
    y, x = max(0, min(y, rows - 1)), max(0, min(x, cols - 1))

    # Calculate integer and fractional parts of coordinates
    x0, x1 = int(x), min(int(x) + 1, cols - 1)
    y0, y1 = int(y), min(int(y) + 1, rows - 1)
    x_frac, y_frac = x - x0, y - y0

    # Get pixel values at the four corners of the surrounding square
    q11, q12, q21, q22 = image[y0][x0], image[y0][x1], image[y1][x0], image[y1][x1]

    value = (q11 * (1 - x_frac) * (1 - y_frac) +
             q12 * x_frac * (1 - y_frac) +
             q21 * (1 - x_frac) * y_frac +
             q22 * x_frac * y_frac)

    return round(value)


def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    """
    Resizes an image to a new size.
    :param image: original image
    :param new_height: new height
    :param new_width: new width
    :return: resized image
    """
    original_height, original_width = len(image), len(image[0])
    new_image = [[0] * new_width for _ in range(new_height)]

    for y in range(new_height):
        for x in range(new_width):
            original_x = x * (original_width - 1) / (new_width - 1)
            original_y = y * (original_height - 1) / (new_height - 1)
            new_image[y][x] = bilinear_interpolation(image, original_y, original_x)

    return new_image


def rotate_left(image: SingleChannelImage) -> SingleChannelImage:
    """
    Rotates a matrix 90 degrees left.
    :param image: original image
    :return: rotated image
    """
    rows, cols = len(image), len(image[0])
    rotated_image = [[0] * rows for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            rotated_image[cols - col - 1][row] = image[row][col]

    return rotated_image


def rotate_90(image: Image, direction: str) -> Image:
    """
    Rotates an image 90 degrees.
    :param image:  original image
    :param direction: rotation direction
    :return: rotated image
    """
    if direction == 'L':
        return rotate_left(image)
    elif direction == 'R':
        return rotate_left(rotate_left(rotate_left(image)))


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    """
    Gets edges of an image.
    :param image: original image
    :param blur_size: blur size
    :param block_size: block size
    :param c: constant to subtract
    :return: image just with edges
    """
    kernel = blur_kernel(blur_size)
    blurred_image = apply_kernel(image, kernel)
    new_image = [[0] * len(image[0]) for _ in range(len(image))]
    for row in range(len(image)):
        for col in range(len(image[0])):
            sub_matrix = create_sub_matrix(blurred_image, (row, col), block_size)
            values = [val for row in sub_matrix for val in row]
            threshold = sum(values) / float(len(values))
            if blurred_image[row][col] < threshold:
                new_image[row][col] = 0
            else:
                new_image[row][col] = 255

    return new_image


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    new_image = [[0] * len(image[0]) for _ in range(len(image))]
    for row in range(len(image)):
        for col in range(len(image[0])):
            new_image[row][col] = round(floor(image[row][col] * N / 256) * 255 / (N - 1))

    return new_image


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print('Run with wrogn number of arguments')
        sys.exit()
    try:
        image = load_image(arguments[0])
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    except PIL.UnidentifiedImageError:
        print('unvalid file')
        sys.exit()

