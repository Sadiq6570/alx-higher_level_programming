#!/usr/bin/python3

'''classes rising error '''


class Square:

    def __init__(self, size=0):
        if not isinstance(size, int):
            ''' instance of size'''
            raise TypeError("size must be integer ")
        elif size < 0:
            '''size of size'''
            raise ValueError("size must be >= 0")
        self.__size = size
