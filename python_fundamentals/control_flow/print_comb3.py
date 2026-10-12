#!/usr/bin/env python3

for left in range(10):
    for right in range(left + 1, 10):
        print("{}{}".format(left, right),
              end="\n" if left == 8 and right == 9 else ", ")
