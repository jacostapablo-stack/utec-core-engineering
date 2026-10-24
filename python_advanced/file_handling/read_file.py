#!/usr/bin/env python3
"""Módulo para leer e imprimir archivos de texto UTF-8."""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    print(content, end="")
