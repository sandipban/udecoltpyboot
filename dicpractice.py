#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:28:28 2019

@author: sandip
"""
personal = {'name': 'sandip', 'age':48, 'prof': 'software', 'isgood': True}
print(personal.values())
for g in personal.values():
    print(g)
for h in personal.keys():
    print(h)
for j in personal.items():
    print(j)
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0,
                 lisa=50.25, harrison=10.0)
total_donations = 0
for x in donations.values():
    total_donations += x
print(total_donations)
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
quantity = bakery_stock.get(food)
if quantity:
    print(f'{quantity} quantity left')
else:
    print('We do not make this')
str1 = 'ABC'
str2 = '123'
combo = {str1[i] : str2[i] for i in range(0,len(str1))}
print(combo)