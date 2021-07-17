from random import randint
from random import choice
a = ['rock','paper','scissors']
b = choice(a)
print(b)
x = randint(-100, 100)
y = randint(-100, 100)
print(x, y)
if x and y:
    if x > 0 and y > 0:
        print('x and y positive')
    elif x < 0 and y < 0:
        print('x and y negative')
    elif x < 0 and y > 0:
        print('x negative and y positive')
    else:
        print('x positive y negative')
