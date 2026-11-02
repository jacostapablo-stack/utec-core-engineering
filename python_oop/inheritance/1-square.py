#!/usr/bin/env python3
"""Define un cuadrado que hereda de Rectangle."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado con tamaño privado."""

    def __init__(self, size):
        """Valida y almacena el tamaño del cuadrado"""
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcula y devuelve el Area del cuadrado."""
        return self.__size * self.__size:
