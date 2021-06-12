#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:33:21 2019

@author: sandip
"""

# *Args practice, purple test.

def contains_purple(*args):
# =============================================================================
    #     for item in args:
    #         if item == 'purple':
    #             return True
    #     return False
    # print(contains_purple('purple' ))
    # =============================================================================
    if 'purple' in args: return True
    return False
print(contains_purple('white','green', 'blue', 34 ))


# **kwargs exercise. Adding prefix and suffix with the word.

def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

print(combine_words('child', suffix = 'ish'))
print(combine_words('John', prefix = 'Mr. '))


# Map time exercise. Decrement a list.

def decrement_list(num):
    new_list = list(map(lambda x : x - 1, num))
    print(new_list)

decrement_list([1, 2, 3])

