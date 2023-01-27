#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - picture_to_pixels.py\n
    Class that converts an image file to a grid of pixels with RGB values\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"


import statistics
from dataclasses import field
from enum import Enum, auto
from typing import Callable

import numpy as np
from PIL import Image

from imgObj_class import imgObj
from user_inputs import get_user_option


class Pixelation_Mode(Enum):
    ALWAYS_MEAN = auto()
    ALWAYS_MODE = auto()
    COND_MIX = auto()


class pic2pix:
    """
    Class: pic2pix \n
    Operator Class to convert image object into pixelated pattern \n
    Author: Edward Hayes
    """

    def __init__(self, image: imgObj, pixel_dims: list):
        self.original = image
        self.pixel_dims = pixel_dims
        self.bin_size = field(init=False)
        self.pixel_rgb = field(init=False)

    def calc_bin_size(self):
        """
        Method to calculate pixel bin size from original and pixel dimensions\n
        """
        dx, dy = self.original.dim_x, self.original.dim_y
        px, py = self.pixel_dims[0], self.pixel_dims[1]
        bin_x, bin_y = int(dx / px), int(dy / py)
        if not bin_x == bin_y:
            print(f"WARNING: Pixel bins not square")
            return
        else:
            self.bin_size = bin_x

    def calc_mean_rgb_pixel_group(self, pix_r, pix_g, pix_b):
        """
        Method to calculate the mean value of RGB values\n
        Values extracted from square area with length bin_size
        """
        r_mean = int(sum(pix_r) / len(pix_r))
        g_mean = int(sum(pix_g) / len(pix_g))
        b_mean = int(sum(pix_b) / len(pix_b))
        mean_rgb = r_mean, g_mean, b_mean
        return mean_rgb

    def calc_stdv_rgb_pixel_group(self, pix_r, pix_g, pix_b):
        """
        Calculate standard deviation of RGB values\n
        Values extracted from square area with length bin_size
        """
        stdv_rgb = (np.std(pix_r), np.std(pix_g), np.std(pix_b))
        return stdv_rgb

    def calc_mode_rgb_pixel_group(self, pix_r, pix_g, pix_b):
        """
        Method to calculate the mode of RGB values\n
        Values extracted from square area corresponding to bin_size
        """
        mode_rgb = (
            statistics.mode(pix_r),
            statistics.mode(pix_g),
            statistics.mode(pix_b),
        )
        return mode_rgb

    def pixel_interpolator(self, x_start, y_start):
        """
        for each bin of pixels, compute RGB: mean, mode, stdev and make a decision\n
        return decision RGB value
        """
        # Create pixel group reference ids
        x_range = [int(i + x_start) for i in range(self.bin_size)]
        y_range = [int(i + y_start) for i in range(self.bin_size)]
        # Retrieve Pixel Group R, G, B's
        pix_r = [self.original.pixels[i, j][0] for i in x_range for j in y_range]
        pix_g = [self.original.pixels[i, j][1] for i in x_range for j in y_range]
        pix_b = [self.original.pixels[i, j][2] for i in x_range for j in y_range]
        # Calculate mean, stdv, mode of pixel group
        mean_rgb = self.calc_mean_rgb_pixel_group(pix_r, pix_g, pix_b)
        stdv_rgb = self.calc_stdv_rgb_pixel_group(pix_r, pix_g, pix_b)
        mode_rgb = self.calc_mode_rgb_pixel_group(pix_r, pix_g, pix_b)
        if sum(stdv_rgb) > 85:
            return mode_rgb
        else:
            return mean_rgb

    def pixel_iterator(self):
        """
        Loops over Pixels in original image to create groups\n
        For Each group executes pic2pix.pixel_interpolator()\n
        Returns array of RGB values stored in pic2pix.pixel_rgb
        """
        height = self.pixel_dims[1]
        width = self.pixel_dims[0]
        channel = 3
        arr = np.full((height, width, channel), [0, 0, 0], dtype=("uint8"))
        for i in range(width):
            for j in range(height):
                x_start = i * self.bin_size
                y_start = j * self.bin_size
                rgb_out = self.pixel_interpolator(x_start, y_start)
                arr[j, i] = list(rgb_out)
        self.pixel_rgb = arr
