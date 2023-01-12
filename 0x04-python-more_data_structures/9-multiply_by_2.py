#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiple = {x:a_dictionary[x]*2 for x in a_dictionary }
#     for i in a_dictionary:
#         multiple[i] = a_dictionary[i] * 2
    return multiple
