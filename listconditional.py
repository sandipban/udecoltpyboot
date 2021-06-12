#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:49:30 2019

@author: sandip
"""
# =============================================================================
# def single_letter_count(word, leter):
#     word = word.lower()
#     leter = leter.lower()
#     number = word.count(leter)
#     if number:
#         return number
#     return 0
# print(single_letter_count('Hello world', 'L'))
#
# =============================================================================
num = [1,2,3,4,5,6]
num = [x**3 for x in num]
print (num)
friends = ['ram', 'shyam', 'jadu', 'madhu']
new_list = [item[0].upper()+item[1:] for item in friends]
print(new_list)
new_list = [item[: : -1].lower() for item in friends]
print(new_list)
board = [[x for x in range(1, 4)] for y in range(1, 4)]
print(board)
newboard = [['X' if x % 2 != 0 else 'O' for x in range(1, 4)] for y in range(1, 4)]
print(newboard)
