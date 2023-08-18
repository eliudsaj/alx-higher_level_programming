#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_sum = 0
    weight_average = 0
    for s, w in my_list:
        weight_average += s * w
        weight_sum += w
    return weight_average / weight_sum
