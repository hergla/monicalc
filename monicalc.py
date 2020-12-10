#!/usr/bin/env python3

import math

ZOLL = 2.54

def calc_dimensions( diagonal, aspect_x, aspect_y):
    faktor = math.sqrt( diagonal**2 / (aspect_x**2 + aspect_y**2))
    width = aspect_x * faktor
    height = aspect_y * faktor
    return width, height

def main():
    diagonal = float(input    ("Diagonal in Inch          : "))
    aspect = input            ("Aspect ratio (e.g. 16:9)  : ")
    pixel_width = int(input   ("Pixels (width)            : "))
    pixel_height = int(input  ("Pixels (height)           : "))
    aspect_x , aspect_y = aspect.split(':')
    width, height = calc_dimensions(diagonal, int(aspect_x), int(aspect_y))
    ppi_x = round(pixel_width / width, 2)
    ppi_y = round(pixel_height / height, 2)

    print(f"Values Inch. -  Width: {round(width,2)}  Height: {round(height,2)}  Diagonal: {diagonal} PPI(x/y): {ppi_x} {ppi_y}")
    print(f"Values cm.   -  Width: {round(width * ZOLL,2)}  Height: {round(height*ZOLL,2)}  Diagonal: {diagonal*ZOLL} PPI(x/y): {ppi_x} {ppi_y}")


if __name__ == '__main__':
    main()
