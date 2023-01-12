#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    b = ''
    for i in a_dictionary:
        if a_dictionary[i] > m:
            m = a_dictionary[i]
            b = i
    return b
#     if not a_dictionary:
#         return None
#     else:
#         new_dict = max(a_dictionary, key=a_dictionary.get)
#         return new_dict
    
