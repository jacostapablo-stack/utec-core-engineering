#!/usr/bin/env python3
"""Módulo para añadir contenido a archivos de texto UTF-8."""


def append_write(filename="", text=""):
    """Añade texto a un archivo y devuelve los caracteres escritos."""
    with open(filename, "a", encoding="utf-8") as file:
        added = file.write(text)

    return added
