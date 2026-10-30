#!/usr/bin/env python3
"""Define la clase Square."""


class Square:
    """Representa un cuadrado con tamaño validao."""
    def __init__(self, size=0):
        """Inicializa y valida el tamaño del cuadrao."""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
    return self.__size * self.__size
