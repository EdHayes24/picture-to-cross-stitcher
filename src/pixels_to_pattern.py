#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - pixels_to_pattern.py\n
    Functions to convert pixel arrays into images and cross-stitch patterns
"""
__author__ = "Edward Hayes"
__status__ = "Development"

import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
from PIL import Image

from imgObj_class import imgObj


class InvalidScaleException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def resize_pixel_array(pix_array: np.array, scale: int):
    """
    Function to increase the size and copy existing data in numpy array\n
    pix_array - np.array, array of values to be epxanded\n
    scale - int, positive integer scale by which to expand the array\n
    Returns: numpy array enlarged by factor of <scale>
    """
    try:
        scale = int(scale)
        if scale <= 1:
            raise InvalidScaleException(scale)
    except ValueError as ve:
        print(
            f"ERR resize_pixel_array(): {ve}\nCannot resize pixel_array to non-integer value {scale}\n"
        )
    except InvalidScaleException as ise:
        print(f"ERR resize_pixel_array(): InvalidScaleError - scale:{ise.value} <= 1")
        print("Cannot resize pixel_array to value <= 1")
    else:
        resized_array = np.repeat(np.repeat(pix_array, scale, axis=1), scale, axis=0)
        return resized_array


def pixel_array_to_plot(pix_array: np.array, scale: int):
    """
    Function to convert pixel array into matplotlib plot with gridlines\n
    pix_array - np.array, numpy array of RGB values\n
    scale - int, no. of pixels per grid square\n
    Returns: ???
    """
    print("Execute: pixel_array_to_plot()\n")
    img = Image.fromarray(pix_array)
    grid_line_width = scale
    fig = plt.figure(
        figsize=(
            float(img.size[0]) / grid_line_width,
            float(img.size[1]) / grid_line_width,
        ),
        dpi=grid_line_width,
    )
    axes = fig.add_subplot(111)
    fig.subplots_adjust(left=0, right=1)
    grid_interval = scale
    location = plticker.MultipleLocator(base=grid_interval)
    axes.xaxis.set_major_locator(location)
    axes.yaxis.set_major_locator(location)
    axes.grid(which="major", axis="both", linestyle="-", color="k")
    axes.imshow(img)
    axes.tick_params(
        left=False, right=False, labelleft=False, labelbottom=False, bottom=False
    )
    # Get colours from pixel array
    cols = np.unique(pix_array.reshape(-1, pix_array.shape[2]), axis=0)
    for col in cols:
        print(f"Colour {col}")
    # Find midpoint of pixel blocks
    pix_x = pix_array.shape[0]
    pix_y = pix_array.shape[1]
    big_pix_x = pix_x // scale
    big_pix_y = pix_y // scale
    for bx in range(big_pix_x):
        for by in range(big_pix_y):
            xctr = int((bx + 0.5) * scale)
            yctr = int((by + 0.5) * scale)
            color = pix_array[xctr][yctr][:]
    # Add markers:
    axes.scatter([50, 100, 150, 50], [150, 100, 50, 10], marker=11)
    fig.savefig("./data/myImageGrid.png", dpi=grid_line_width)


if __name__ == "__main__":
    print("pixels_to_patterns.py >>> Execute")
    pic = Image.open("./data/pop-test.jpeg")
    pix = np.array(pic)
    pix = resize_pixel_array(pix_array=pix, scale=100)
    print(pix.shape)
    pixel_array_to_plot(pix, 100)
    # add_grid_pixel_array(pix, 3)
    # Let's make a simple plot
    # im = Image.fromarray(pix)
    # plt.figure()
    # fig = plt.imshow(im)
    # ax = plt.gca()
    # xticks = np.arange(0, im.size[0] + 1, 100)
    # yticks = np.arange(0, im.size[1] + 1, 100)
    # ax.set_xticks(xticks)
    # ax.set_yticks(yticks)
    # ax.set_xticklabels([])
    # ax.set_yticklabels([])
    # ax.grid()
    # plt.savefig("./data/bigpic.png")
