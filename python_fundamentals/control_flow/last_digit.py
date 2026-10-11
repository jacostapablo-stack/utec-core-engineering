#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
magnitude = abs(number) % 10
signed_digit = -magnitude if number < 0 else magnitude
if signed_digit > 5:
    print("Last digit of", number, "is", signed_digit, "and is greater than 5")
elif signed_digit == 0:
    print("Last digit of", number, "is", signed_digit, "and is 0")
else:
    print(
            "Last digit of",
            number,
            "is",
            signed_digit,
            "and is less than 6 and not 0"
            )
