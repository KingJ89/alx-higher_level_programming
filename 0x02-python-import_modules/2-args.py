#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of arguments"""
    import sys

    arguments = sys.argv[1:]
    count = len(arguments)

    # Print the number of arguments
    print(f"{count} {'argument' if count == 1 else 'arguments'}:")

    # Print each argument with its index
    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")
