#!/usr/bin/python3

"""Read from file"""
def read_file(filename=""):
    with open(filename) as file:
        print(file.read(), end="")

        if __name__ == "__main__":
            read_file(my_file_0.txt)
