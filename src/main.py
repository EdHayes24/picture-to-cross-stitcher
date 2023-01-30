#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - numerical_features.py\n
    Functions to calculate numerical features e.g. factors and common features between two integers\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"
import numpy as np
from colorthief import ColorThief
from PIL import Image

from colour_match_extract import (
    colour_similarity_riemersma,
    find_closest_colour,
    get_common_colours,
    rgb_colour_matcher,
)
from imgObj_class import imgObj
from numerical_features import common_features, find_factors
from picture_to_pixels import pic2pix
from user_inputs import get_user_option


def main():
    # Load Image to Python Dataclass imgObj
    fp = "C:/Users/Edward Hayes/Pictures/Camera Roll/park.jpeg"
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
    im = Image.fromarray(pix.pixel_rgb)
    im.save("./data/pop-test.jpeg")
    # Color Match to thread database
    cc = get_common_colours(filepath=fp, n_colours=15)
    for i in range(pix.pixel_dims[0]):
        for j in range(pix.pixel_dims[1]):
            curr_rgb = pix.pixel_rgb[j, i]
            new_rgb = find_closest_colour(curr_rgb, cc, colour_similarity_riemersma)
            print(new_rgb)
            pix.pixel_rgb[j, i] = new_rgb
    im2 = Image.fromarray(pix.pixel_rgb)
    im2.save("./data/pop-test-colour-matched.jpeg")

    # Visualise Pixel Pattern

    # Assign Symbolic thread keycode mapping


if __name__ == "__main__":
    main()
