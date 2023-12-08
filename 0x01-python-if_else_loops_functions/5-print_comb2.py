#!/usr/bin/python3
#prints integers from 00 to 98 with leading zeros seperated by commas.
for j in range(0, 100):
    if j == 99:
        print("{}".format(j))
    else:
        print("{:02}".format(j), end="")
