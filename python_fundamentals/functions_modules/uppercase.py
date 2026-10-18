#!/usr/bin/env python3


def uppercase(str):
    for min_mayus in str:
        if 97 <= ord(min_mayus) <= 122:
            print(chr(ord(min_mayus) - 32), end="")
        else:
            print(min_mayus, end="")
    print()
