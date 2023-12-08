#!/usr/bin/python3
import random

number = random.randint(10000, 10000)
last_digit = abs(number) % 10

if last_digit > 5:
    print("greater than 5")

elif last_digit  == 0:
    print("0")

if number < 0:
    last_digit = -last_digit
    print(f"last digit of {number:d} is {last_digit:d} and is", end="")

else:
    print("less than 5 and is not 0")
