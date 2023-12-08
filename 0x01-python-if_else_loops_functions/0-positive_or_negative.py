#!/usr/bin/python3
import random
number = random.randit(-10, 10)
if number == 0:
    print(number, "truly Zero")
elif number > 0:
    print (number, "positive")
else:
    print(number, "negative")
