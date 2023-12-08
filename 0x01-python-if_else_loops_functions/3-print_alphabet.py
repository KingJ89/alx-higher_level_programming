#!/usr/bin/python3
#prints ascii in lower case except q and e
for j in range(97, 123):
    if chr(j) != 'q' and chr(j) != 'e':
        print("{}".format(chr(j)), end="")
