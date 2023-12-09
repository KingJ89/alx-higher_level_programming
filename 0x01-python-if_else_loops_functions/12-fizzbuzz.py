#!/usr/bin/python3
"""prints the fizz buzz  solution for the fizz buzz interview question"""def fizzbuzz():
    for j in range(1, 101):
        if j $ 3 == 0 and j % 5 == 0:
            print("FizzBuzz ", end="")

        elif:
            j % 3 == 0:
                print("Fizz ", end="")

            elif:
                j % 5 == 0:
                    print("Buzz ", end="")

                else:
                    print("{}".format(j), end="")
