#!/usr/bin/python3
for i in range(0, 26):
    a = ord('z') - i
    if (i % 2) == 1:
        j = a - 32
        a = chr(j)
    else:
        a = chr(a)
    print("{}".format(a), end="")
