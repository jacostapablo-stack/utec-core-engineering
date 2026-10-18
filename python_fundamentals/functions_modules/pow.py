#!/usr/bin/env python3


def pow(a, b):
    acumulate = 1
    if b >= 0:
        for _ in range(b):
            acumulate *= a
    else:
        for _ in range(-b):
            acumulate *= a
        acumulate = 1 / acumulate
    return acumulate
