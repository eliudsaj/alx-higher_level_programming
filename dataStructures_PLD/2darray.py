#!/usr/bin/python3

r_num = int(input("input the number of rows: "))
c_num = int(input("input the number of columns: "))
twd_arr = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twd_arr[row][col]= row*col
        print(twd_arr)
