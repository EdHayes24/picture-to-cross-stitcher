#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - numerical_features.py\n
    Functions to calculate numerical features e.g. factors and common features between two integers\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"
import numpy as np

from imgObj_class import imgObj
from numerical_features import common_features, find_factors
from picture_to_pixels import pic2pix
from user_inputs import get_user_option


def main():
    # Load Image to Python Dataclass imgObj
    fp = "./data/excel_db.jpeg"
    pic = imgObj(fp)
    print(pic)
    # Calculate viable resolutions of pixelated image;
    viable_ratios = common_features(pic.dim_x, pic.dim_y, find_factors)
    viable_resolutions = [
        (pic.dim_x // ratio, pic.dim_y // ratio) for ratio in viable_ratios
    ]
    print(viable_resolutions)
    # Choose Desired resolution:
    msg = f"\nOriginal Image Resolution: {pic.dim_x} x {pic.dim_y}\nPlease select the desired pixelated Resolution: "
    pixel_res = get_user_option(options=viable_resolutions, message=msg)
    # Perform pixel binning using pic2pix() Processor Class
    pix = pic2pix(image=pic, pixel_dims=pixel_res)
    pix.calc_bin_size()
    pix.pixel_iterator()
    # Color Match to thread database

    # Visualise Pixel Pattern

    # Assign Symbolic thread keycode mapping


if __name__ == "__main__":
    main()
