import random

HEADS = 1
TAILS = random.randint(3,10)

headCount = 0
tailCount = 0

for counter in range(11):

    outcome = random.randrange(HEADS, TAILS)
    if (outcome == HEADS):
        print("HEADS")
        headCount = headCount + 1
    else:
        print("TAILS")
        tailCount = tailCount + 1