# modules.py

#!/usr/bin/env python3

""" modules.py - an example of Python modules """

__counter = 0


def sum_lst(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum


def product_lst(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod


if __name__ == "__main__":
    print("I prefer to be a modules, but I can do some tests for you")
    lst = [i + 1 for i in range(5)]
    print(sum_lst(lst) == 15)
    print(product_lst(lst) == 120)
