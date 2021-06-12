# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file"""
friends = ['ram', 'shyam', 'jadu']
friends = [item[0].upper() + item[1:] for item in friends]
print(friends)
with_vowels = 'This is so much fun!'
without_vowels = ''.join(char for char in with_vowels if char not in'aeiou')
print(without_vowels)
list_one = [1, 2, 3, 4]
list_two = [3, 4, 5, 6]
list_name = ['Tim', 'Ellie', 'Matt']
common_of_onetwo = [common for common in list_one if common in list_two]
print(common_of_onetwo)
reversed_name = [item[::-1].lower()for item in list_name]
print(reversed_name)
answer = [num for num in range(1, 101) if num % 12 == 0]
print(answer)
word = 'amazing'
withoutvow = [letter for letter in word if letter not in 'aeiou']
print(withoutvow)
artist = {'first_name' : 'Sandhya', 'last_name': 'Roy'}
name = f"{artist['first_name']} { artist['last_name']}"
print(name)