import random

p1c1rank = random.randrange(1,14)
p1c1suit = random.randrange(1,5)

p1c2rank = random.randrange(1,14)
p1c2suit = random.randrange(1,5)

points = 0
bonuspoints = 0

if ((p1c1rank == 1) and (p1c2rank != 1)):