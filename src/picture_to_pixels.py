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

import numpy as np

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
        x_range = [int(i + x_start) for i in range(self.bin_size)]
        y_range = [int(i + y_start) for i in range(self.bin_size)]
        print(x_range)
        print(y_range)
        if x_start > 8:
            A = 1 / 0
        pix_r = [self.original.pixels[i, j][0] for i in x_range for j in y_range]
        pix_g = [self.original.pixels[i, j][1] for i in x_range for j in y_range]
        pix_b = [self.original.pixels[i, j][2] for i in x_range for j in y_range]
        mean_rgb = self.calc_mean_rgb_pixel_group(pix_r, pix_g, pix_b)
        stdv_rgb = self.calc_stdv_rgb_pixel_group(pix_r, pix_g, pix_b)
        mode_rgb = self.calc_mode_rgb_pixel_group(pix_r, pix_g, pix_b)
        print(f"{x_start},{y_start}:{x_start+self.bin_size},{y_start+self.bin_size}")
        print(mean_rgb)
        print(stdv_rgb)
        print(mode_rgb)

    def pixel_iterator(self):
        #
        x_start = 0
        y_start = 0
        self.pixel_interpolator(x_start, y_start)
        for i in range(int(self.original.dim_x / self.bin_size)):
            x_start += self.bin_size
            for j in range(int(self.original.dim_y / self.bin_size)):
                print(f"x:{x_start}, y:{y_start}")
                y_start += self.bin_size
                self.pixel_interpolator(x_start, y_start)


# dd = desired_dimension_selector(common_factors(im.size[0], im.size[1]), im.size)
# print(dd)
# # With selected dimensions, make blocks of data in matrix:
# x_size = int(im.size[0] / dd[0])
# y_size = int(im.size[1] / dd[1])
# pix_r = [pix[i,j][0] for i in range(x_size) for j in range(y_size)]
# pix_g = [pix[i,j][1] for i in range(x_size) for j in range(y_size)]
# pix_b = [pix[i,j][2] for i in range(x_size) for j in range(y_size)]
# # Calc Mean, Stdev, mode. If sd is high, select mode instead?
# mean_rgb = (sum(pix_r) / len(pix_r), sum(pix_g) / len(pix_g), sum(pix_b) / len(pix_b))
# stdv_rgb = (np.std(pix_r), np.std(pix_g), np.std(pix_b))
# mode_rgb = (statistics.mode(pix_r),statistics.mode(pix_g),statistics.mode(pix_b))
# print(mean_rgb)
# print(stdv_rgb)
# print(mode_rgb)
