#!/usr/bin/python3

        if __name__ == "__main__":
        """Prints Sum of all arguments"""
        import sys

        total = 0
        for j in range(len(sys.argv) - 1):
        total += int(sys.argv[j + 1])
        print("{}".format(total))
