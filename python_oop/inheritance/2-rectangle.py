#!/usr/bin/env python3
"""Define un rectángulo que hereda de BaseGeometry."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con ancho y altura privados."""

    def __init__(self, width, height):
        """Valida y almacena el ancho y la altura del rectángulo."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
