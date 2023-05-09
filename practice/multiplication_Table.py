#!/usr/bin/python3
import random
import math

mulTable = [[0] * 10 for i in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        mulTable[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(mulTable[i][j], end=", ")
    print()
