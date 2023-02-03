#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - colour_match_extract.py\n
    Functions to retrieve most common colours and match to array of RGBs
"""
__author__ = "Edward Hayes"
__status__ = "Development"

import numpy as np
from colorthief import ColorThief
from PIL import Image


def get_common_colours(filepath: str, n_colours: int):
    """
    Function to retrieve most common n_colours from an image file\n
    Requires colorthief package\n
    filepath - str, path to image file\n
    n_colours - int, maximum number of colours to extract\n
    Returns: List of colours
    """
    color_thief = ColorThief(filepath)
    palette = color_thief.get_palette(color_count=n_colours, quality=1)
    return palette


def rgb_colour_matcher(colour_to_match, available_colours):
    """
    Function to find closest matching colour in list of RGB values\n
    colour_to_match - list of int, RGB colour
    available_colours - list of tuples, RGB colours to match from
    Returns: closest colour RGB value
    """
    palette = np.array(available_colours)
    target = np.array(colour_to_match)
    square_sum = np.sum((palette - target) ** 2, axis=1)
    root_square = np.sqrt(square_sum)
    min_idx = np.where(root_square == np.amin(root_square))
    nearest_colour = palette[min_idx]
    return nearest_colour[0]


def colour_similarity_riemersma(colour, col_options):
    """
    Compromise to the RGB colour matcher\n
    See: https://www.compuphase.com/cmetric.htm \n
    """
    palette = np.array(col_options)
    target = np.array(colour)
    squares = (palette - target) ** 2
    red_squares = squares[:, 0]
    green_squares = squares[:, 1]
    blue_squares = squares[:, 2]
    mean_red = ((palette + target) / 2)[:, 0]
    color_proximity = np.sqrt(
        ((2 + (mean_red / 256)) * red_squares)
        + 4 * green_squares
        + blue_squares * (2 + ((255 - mean_red) / 256))
    )
    return color_proximity


def find_closest_colour(colour, col_options, match_method=colour_similarity_riemersma):
    """
    Compromise to the RGB colour matcher\n
    See: https://www.compuphase.com/cmetric.htm \n
    """
    color_proximity = match_method(colour, col_options)
    min_idx = np.where(color_proximity == np.amin(color_proximity))
    nearest_color = np.array(col_options)[min_idx]
    return nearest_color


def most_divergent_colours(
    col_options, n_colours, force_include, match_method=colour_similarity_riemersma
):
    """
    Function to identify the combination of RGB color codes which are most different\n
    col_options = list of RGB codes of colours to choose from\n
    n_colours = no. of colours to keep\n
    force_include = no. of colours must be kept, reads first force_include from col_options\n
    Returns: optimised combination
    """
    # Get all possible combinations using itertools
    colour = (256, 256, 256)
    # Calculate Metric For each combination
    color_proximity = match_method(colour, col_options)
    # maximise color_proximity calculated
    # lookup optimisation functions


if __name__ == "__main__":
    print("colour_match_extract.py")
    img_colou = get_common_colours(filepath="./data/excel_db.jpeg", n_colours=15)
    colou = [110, 150, 13]
    print(img_colou)
    best_match = find_closest_colour(colou, img_colou, colour_similarity_riemersma)
    print(best_match, colou)
