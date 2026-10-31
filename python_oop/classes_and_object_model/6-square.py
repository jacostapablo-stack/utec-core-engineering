#!/usr/bin/env python3
"""Define la clase Square."""


class Square:
    """Representa un cuadrado con tamaño y posición validados."""
    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el tamaño y la posición del cuadrado."""
        self.size = size
        self.position = position

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size * self.__size

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, size):
        """Valida y modifica el tamaño del cuadrado."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        """Devuelve la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y modifica la posición del cuadrado."""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def __str__(self):
        """Devuelve la representación del cuadrado como cadena."""
        if self.__size == 0:
            return ""

        rows = [
            " " * self.__position[0] + "#" * self.__size
            for _ in range(self.__size)
        ]

        result = "\n".join(rows)
        return "\n" * self.__position[1] + result

    def my_print(self):
        """Imprime el cuadrado según su tamaño y posición."""
        print(self)
