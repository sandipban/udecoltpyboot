i = 0
for n in range(10, 20):
    if n % 2 != 0:
        i += n
print(i)

x = 0

# YOUR CODE GOES HERE:
for n in range(11, 21, 2):
    x += n
print(x)
#Section 10, exercise 86
#Fnrom 1 to 20 print all odd and even number like 3 is odd, 4, and 13 should be written unlucky.
for n in range(1, 21):
    if n == 4 or n == 13:
        print(f'{n} is unlucky')
    elif n % 2 == 0 :
        print(f'{n} is even')
    else:
        print(f'{n} is odd')