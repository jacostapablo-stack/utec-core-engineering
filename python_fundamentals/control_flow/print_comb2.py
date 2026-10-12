#!/usr/bin/env python3

for twodig in range(99 + 1):
    print("{0:02d}".format(twodig),
          end=", " if twodig < 99 else "\n")
