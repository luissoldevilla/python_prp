import random

countEven = 0
countOdd = 0

for count in range(100):
    number = random.randint(0, 101)
    print(number)
    if (number % 2) == 0:
        countEven += 1
    else:
        countOdd += 1
