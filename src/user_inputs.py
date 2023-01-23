#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - user_inputs.py\n
    Utility functions to retrieve custom user inputs\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"

def get_user_option(options:list, message:str="\n", err_msg:str="\n"):
    '''
    Prints options for user to select from alongside input message\n
    options - list, choices for user to pick from \n
    message - str, instructions to print for user input \n
    err_msg - str, updates on execution after input error
    Returns: Value corresponding to selected option\n
    Author: Edward Hayes 
    '''
    while True:
        print(message)
        print(err_msg)
        for i, option in enumerate(options):
            print(f"{i} = {option}")
        try:
            choice = input("Please enter the ID of the desired option or type 'X' to abort: ")
            if choice == "x" or choice == "X": 
                print("No choice selected, aborting choice")
                break
            choice = int(choice) 
            print(f"You have selected: {options[choice]}")
        except IndexError as ide:
            print(f"Error {ide}")
            err_msg = f"*** Please enter an integer value within {range(len(options))}"
        except Exception as e:
            print(f"Error {e}")
        else:
            return options[choice]