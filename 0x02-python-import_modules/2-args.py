#!/usr/bin/python3

if __name__ == "__main__":

    #print number of list of args
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 args.")
    elif count == 1:
        print("1 args:")
    else:
        print("{} args:" .format(count))
        for i in range(count):
            print("{}: {}" .format(i + 1, sys.argv[i + 1]))
