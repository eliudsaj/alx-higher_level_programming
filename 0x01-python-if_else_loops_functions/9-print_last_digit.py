#!/usr/bin/python3
def print_last_digit(number):
    char = int(repr(number)[-1])
    print("{}".format(char), end="")
    return char
