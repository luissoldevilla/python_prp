#  Write a program that generates 100 random numbers 
# and keeps a count of how many of those random 
# numbers are even, and how many of them are odd.

# The problem solution:

import random

countEven = 0
countOdd = 0
count4 = 0
count5 = 0


for count in range(100):
    number = random.randint(0, 101)
    number1 = random.randint(0, 101)
    print(number)
    if (number % 2) == 0:
        countEven += 1
    else:
        countOdd += 1

print('Numbers of Even:', countEven)
print('Numbers of Odd:', countOdd)