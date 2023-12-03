if __name__ == "__main__":
    #print the sum, difference, multiple and quotientof 10 and 5.
    from calculator_1 import add, div, mul, sub

    a = 10
    b = 5

    print("{} + {} = {}".fomat(a, b, add(a, b)))
    print("{} + {} = {}".fomat(a, b, sub(a, b)))
    print("{} + {} = {}".fomat(a, b, mul(a, b))) 
    print("{} + {} = {}".fomat(a, b, div(a, b)))
