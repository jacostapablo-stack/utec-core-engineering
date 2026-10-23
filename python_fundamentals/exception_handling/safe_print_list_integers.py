#!/usr/bin/env python3


def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    position = 0
    while position < x:
        try:
            print("{:d}".format(my_list[position]), end="")
            printed += 1
        except (ValueError, TypeError):
            pass
        position += 1
    print()
    return printed
