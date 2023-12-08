#!/usr/bin/python3
#print pairs of values j, m where j is less than m and seperated by commas
for j in range(0, 10):
    for m in range(j + 1, 10):
        if j == 8 and m == 9:
            print("{}{}".format{j, m))
        else:
            print("{}{}".format(j, m), end=",")
