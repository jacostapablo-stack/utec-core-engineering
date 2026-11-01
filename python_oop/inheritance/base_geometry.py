#!/usr/bin/env python3
"""Define el módulo base para figuras geométricas."""


class BaseGeometry:
    """Representa una clase base para figuras geométricas."""

    def area(self):
        """Lanza una excepción porque el cálculo del área
        no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero positivo."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
