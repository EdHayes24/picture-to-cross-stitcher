#!/usr/bin/env python
""" 
    picture-to-cross-stitcher - imgObj_class.py\n
    Class to store loaded image object in Python\n
"""
__author__ = "Edward Hayes"
__status__ = "Development"

from dataclasses import dataclass, field

from PIL import Image


@dataclass
class imgObj:
    """
    Class: imgObj\n
    Image object input from file\n
    Author: Edward Hayes
    """

    filepath: str
    img: Image = field(init=False)
    dim_x: int = field(init=False)
    dim_y: int = field(init=False)
    pixels: Image = field(init=False)

    def open_image_file(self):
        """
        Method to retrieve and set PIL.Image object to attribute\n
        """
        try:
            img = Image.open(self.filepath)
        except FileNotFoundError as fnfe:
            print(f"imgObj.open_image_file ERROR: File Not Found {fnfe}")
        except Exception as e:
            print(f"imgObj.open_image_file ERROR: {e}")
        else:
            print(f"Image at {self.filepath} successfully retrieved")
            self.img = img

    def load_image_pixels(self):
        """
        Method to obtain RBG pixel values from opened image\n
        """
        if self.img is None:
            print(f"Image {self.filepath} has not been successfully loaded")
            print("Please refer to Method: imgObj.open_image_file()")
            return
        try:
            pixels = self.img.load()
        except Exception as e:
            print(f"imgObj.load_image_pixels ERROR: {e}")
        else:
            print(f"Pixels of Image {self.filepath} successfully loaded")
            self.pixels = pixels

    def get_image_dimensions(self):
        """
        Method to obtain size in pixels of opened image\n
        """
        if self.img is None:
            print(f"Image {self.filepath} has not been successfully loaded")
            print("Please refer to Method: imgObj.open_image_file()")
            return
        try:
            dimensions = self.img.size
        except Exception as e:
            print(f"imgObj.get_image_dimensions ERROR: {e}")
        else:
            print(f"Image {self.filepath} has dimensions {dimensions}")
            self.dim_x = int(dimensions[0])
            self.dim_y = int(dimensions[1])

    def __post_init__(self):
        self.open_image_file()
        self.load_image_pixels()
        self.get_image_dimensions()


if __name__ == "__main__":
    fp = "./data/excel_db.jpeg"
    an_image = imgObj(fp)
    print(an_image)
