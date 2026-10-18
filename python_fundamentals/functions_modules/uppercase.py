#!/usr/bin/env python3


def uppercase(str):
    resultado = ""
    for min_mayus in str:
        if 97 <= ord(min_mayus) <= 122:
            resultado += chr(ord(min_mayus) - 32)
        else:
            resultado += min_mayus
    print(resultado)
