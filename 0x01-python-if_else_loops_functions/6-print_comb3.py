#!/usr/bin/python3

for i in range(00, 90):
    for j in range(i + 1, 100):
        print("{:02d} {:02d}{}".format(i, j, ", " if i != 98 else "\n"), end="")