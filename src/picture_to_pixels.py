#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - picture_to_pixels.py\n
    Class that converts an image file to a grid of pixels with RGB values\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"


import numpy as np

from imgObj_class import imgObj
from numerical_features import common_features, find_factors
from user_inputs import get_user_option


class pic2pix:
    """
    Class: pic2pix \n
    Operator Class to convert image object into pixelated pattern \n
    Author: Edward Hayes
    """

    def __init__(self, image: imgObj):
        self.image = image

    def hello():
        pass

    def calc_pixel_group_mean_rgb(self):
        if self.image.dimensions is None:
            print(f"ERROR pic2pix.calc_pixel_group_mean_rgb() ")
            print(f"pic2pix.image.dimensions = {self.image.dimensions}")
        try:
            print("hello world")
        except Exception as e:
            print(f"{e}")

    def calc_pixel_group_mode_rgb(self):
        pass


def desired_dimension_selector(resolutions: list, img_dims: tuple):
    """
    Function to ask user which resolution they would prefer from the available options\n
    resolutions - list of int, common factors of image dimensions \n
    img_dims - tuple of int, pair of image dimesions x,y \n
    Returns \n
    Author: Edward Hayes
    """
    cs_dims = [tuple(np.divide(img_dims, res)) for res in resolutions]
    desired_dims = get_user_option(cs_dims, "Please Select the desired dimensions: \n")
    return desired_dims


if __name__ == "__main__":
    ## OOP
    pic = imgObj("./data/excel_db.jpeg")
    pic.open_image_file()
    pic.load_image_pixels()
    pic.get_image_dimensions()
    # Get Factors of image dimensions
    pixel_dim_factors = common_features(
        pic.dimensions[0], pic.dimensions[1], find_factors
    )
    # Make user pick desired dimensions
    pattern_dims = desired_dimension_selector(pixel_dim_factors, pic.dimensions)
    # Using selected dimensions, get pixel bork sizes
    pixel_step_size = [
        int(real / patt) for real, patt in zip(pic.dimensions, pattern_dims)
    ]
    print(pixel_step_size)
    # Iterate over
    print(type(pic.img))

    ## FP
    # im = Image.open('./data/excel_db.jpeg')
    # pix = im.load()
    # print(im.size)
    # print(pix[0,0])
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
