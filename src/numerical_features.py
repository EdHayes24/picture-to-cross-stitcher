#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - numerical_features.py\n
    Functions to calculate numerical features e.g. factors and common features between two integers\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"

import math
from typing import Callable


def find_factors(num: int):
    """
    Function to find list of each number by which it divides exactly\n
    num = number to find the factors of\n
    max_value = maximum value of a factor we are interested in\n
    Author: Edward Hayes
    """
    factors = []
    # Max factor = sqrt(num)
    max_factor = int(math.sqrt(num))
    for i in range(1, max_factor + 1):
        if i in factors:
            break
        if num % i == 0:
            factors.append(int(i))
            factors.append(int(num / i))
    return factors


def common_features(num1: int, num2: int, numerical_feature: Callable):
    """
    Function to obtain common numerical features between numbers num1 & num2 \n
    numerical_feature: function to execute on integer, returns list or values \n
    Returns: List of common features in ascending order \n
    Author: Edward Hayes
    """
    f1 = numerical_feature(num1)
    f2 = numerical_feature(num2)
    # cf = [fac for fac in f1 if fac in f2]
    cf = list(set(f1).intersection(f2))
    cf.sort()
    return cf


if __name__ == "__main__":
    alpha = 124
    beta = 256
    fac_alpha = find_factors(alpha)
    fac_beta = find_factors(beta)
    fac_both = common_features(alpha, beta, find_factors)
    print(fac_alpha)
    print(fac_beta)
    print(fac_both)
