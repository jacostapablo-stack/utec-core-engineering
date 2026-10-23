#!/usr/bin/env python3


def safie_print_integer(value):
    try:
        print("{:d}".format(value))
    except(ValueError, TypeError):
        return False

    return True
