__package__ = "tello-quad"
__version__ = "0.1.20"
__debug = True

import pygame

def return_package_details():
    if __debug:
        print(__package__, __version__)
    return (__package__ , __version__)

if __name__ == "__main__":
    return_package_details()
