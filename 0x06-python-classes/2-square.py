#!/usr/bin/python3

'''classes rising error '''


class Square:

    def __init__(self, size=0):
        if size != isinstance(size, int):
            raise TypeError
        print("size must be integer ")
        if size > 0:
            raise ValueError
        print("size must be >= 0")
