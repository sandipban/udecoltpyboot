# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil"""


def generate_evens():
    print([x for x in range(1, 50) if x % 2 == 0])


generate_evens()


def return_day(number):
    if number >= 1 and number <= 7:
        name_dict = {1:'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5
                    : 'Thursday', 6: 'Friday', 7: 'Saturdady'}
        return name_dict.get(number)
    return None
print(return_day(1))


# counting letters in words
# =============================================================================
# def count_letter(word, letter):
#     word = word.lower()
#     letter = letter.lower()
#     count = 0
#     for char in word:
#         if char == letter:
#             count += 1
#     return count
#     return 0
#
# print(count_letter('common column material', 'o'))
#
# =============================================================================

# Alternate way of solving


def count_letter(word, letter):
    word = word.lower()
    letter = letter.lower()
    number = word.count(letter)
    if number:
        return number
    return 0


print(count_letter('common column material', 'n'))


'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1,
'w': 1}'''
def multiple_letter_count(string):
    string = string.lower().replace(" ", "")
    return {letter: string.count(letter) for letter in string}


print(multiple_letter_count('commoN Column'))


'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''
def list_manipulation(lst, command, location, value = None):
    if(command == 'remove' and location == 'end'):
        return lst.pop()
    elif(command == 'remove' and location == 'beginning'):
        return lst.pop(0)
    elif(command == 'add'and location == 'beginning'):
        lst.insert(0, value)
        return lst
    elif(command == 'add' and location == 'end'):
        lst.append(value)
        return lst


print(list_manipulation([1,2,3], "add", "end", 30))



# IS Palindrome?
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string[:] == string[: : -1]:
        return True
    return False


print(is_palindrome('a man a plan a canal Panama'))


'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''
def frequency(lst, primi):
    count = 0
    for number in lst:
        if number == primi:
            count += 1
    return count

print(frequency([1,2,3,4,4,4], 4))


'''
multiply_even_numbers([2,3,4,5,6])
 # 48
'''
def multiply_even_numbers(lst):
    if any(n % 2 == 0 for n in lst):
        total = 1
        for x in [y for y in lst if y % 2 == 0]:
            total*=x
        return total
    return 'There is no even number in the list'


print(multiply_even_numbers([9,3,5,11,2,8,4,64]))


'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


def capitalize(string):
    return string[0].upper() + string[1:]


print(capitalize("tim"))


'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(lst):
# =============================================================================
#     truthy = []
#     for value in lst:
#         if value:
#             truthy.append(value)
#     return truthy
#
# =============================================================================
    return[l for l in lst if l]


print(compact([0,1,2,"",[], False, {}, None, "All done"]))

'''
Find the intersection of two lists
'''

def intersection(lst1, lst2):
    return[l for l in lst1 if l in lst2]

print(intersection([1,2,3], [2,3,4]))
print(intersection(['a','b','c','d','k','z','l'], ['l','z','c','d','a']))


'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def isEven(num):
    return num % 2 == 0

def partition(lst, isEven):
    return[[x for x in lst if isEven(x)], [y for y in lst if not isEven(y)]]


print(partition([1,2,3,4], isEven))
