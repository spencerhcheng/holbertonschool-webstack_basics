#!/usr/bin/python3


class Square(object):
    def __init__(self, size=0):
        """
        Instantiation with required size
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets square size
        """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        """
        Calculate and return size of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints square as hash representation
        """
        if self.__size == 0:
            print()

        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print('#', end="")
                print('#')
