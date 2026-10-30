#!/usr/bin/env python3
"""Define la clase Square."""


class Square:
    """Representa un cuadrado con tamaño validado."""
    def __init__(self, size=0):
        """Inicializa y valida el tamaño del cuadrado."""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size * self.__size

    def get_size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    def set_size(self, size):
        """Valida y modifica el tamaño del cuadrado."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
