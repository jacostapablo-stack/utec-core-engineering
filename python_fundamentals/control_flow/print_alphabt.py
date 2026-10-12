#!/usr/bin/env python3
az = ""

for alfabet in range(ord("a"), ord("z") + 1):
    if chr(alfabet) in "eq":
        continue
    az += chr(alfabet)

print(az)
