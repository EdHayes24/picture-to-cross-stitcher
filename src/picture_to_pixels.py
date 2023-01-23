#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - picture_to_pixels.py\n
    Class that converts an image file to a grid of pixels with RGB values\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"

import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image


class pic2pix():
    '''
    Class: pic2pix \n
    Converts an Image object to a table of pixels with RBG values\n
    Author: Edward Hayes
    '''

    def __init__(self, attribute2):
        self.pixel_dimension = None
        self.attribute2 = attribute2
    
    def some_method():
        ''' 
        Description of Method
        '''
        pass

def find_factors(num:int, max_value:int=None):
    '''
    Function to find list of each number by which it divides exactly\n
    num = number to find the factors of\n
    max_value = maximum value of a factor we are interested in\n
    Author: Edward Hayes
    '''
    factors = []
    # Max factor = sqrt(num)
    max_factor = int(math.sqrt(num))
    for i in range(1,max_factor+1):
        if i in factors:
            break
        if num % i == 0:
            factors.append(int(i))
            factors.append(int(num / i))
    return(factors)

def common_factors(num1:int, num2:int):
    '''
    Function to obtain common factors between numbers num1 & num2 \n
    Returns: List of common factors in ascending order \n
    Author: Edward Hayes
    '''
    f1 = find_factors(num1)
    f2 = find_factors(num2)
    #cf = [fac for fac in f1 if fac in f2]
    cf = list(set(f1).intersection(f2))
    cf.sort()
    return(cf)


if __name__ == "__main__":
    im = Image.open('./data/edh_park_jpg.jpeg')
    pix = im.load()
    print(im.size)
    print(pix[0,0])
    print(common_factors(1440,1080))