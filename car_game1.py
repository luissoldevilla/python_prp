import random

p1c1rank = random.randrange(1,14)
p1c1suit = random.randrange(1,5)

p1c2rank = random.randrange(1,14)
p1c2suit = random.randrange(1,5)

points = 0
bonuspoints = 0

if ((p1c1rank == 1) and (p1c2rank != 1)):

    points = 20 + p1c2rank

elif (p1c1rank != 1) and (p1c2rank == 1):

    points = p1c1rank + 20

elif (p1c1rank == 1) and (p1c1rank == 1):

    points = 40

else:
    points = p1c1rank + p1c2rank

print(p1c1rank)
print(p1c2rank)
print(points)
print(p1c1suit, p1c2suit)

bonuspoints = points
