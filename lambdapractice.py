#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:05:56 2019

@author: sandip
"""

def remove_negatives(l):
    return list(filter(lambda x: x >= 0, l))


print(remove_negatives([-1, 3, 4, -99,0, -44, 5, 7]))


# Generator practice test.

def is_all_strings(lst):
    return all(type(l) == str for l in lst)


print(is_all_strings(['a', 'b', 'c', 'D',2]))