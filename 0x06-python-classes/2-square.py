#!/usr/bin/python3

'''classes rising error '''


class Square:

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be integer ")
        elif size < 0:
            raise ValueError("size must be >= 0")
