#!/usr/bin/python3


def add_integer(a, b=98):
      
      """adding two integers.
      a  must be integer 
      and also b muust be integer 
        Rises eror|:
        if a and b are not int or float.
        Return:
        sum of a and be 
       
      """
      if a != type(int,  float):
            raise TypeError("a must be an interger")
      if b not in (int, float):
            raise TypeError("b must be an integer")
      return int(a) + int(b)


if __name__ == "__main__":
        import doctest
