#!/usr/bin/python3
def uppercase(str):
    char = list(str)
    for i in range(len(char)):
        if (ord(char[i]) > 96 and ord(char[i]) < 123):
            char[i] = chr(ord(char[i]) - 32)
    print("{}".format(("").join(char)))
