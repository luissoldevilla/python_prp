# we expoprt the library random
import random

total = 0
dieroll = 0
diescore1 = 0
diescore2 = 0

diescore1 = random.randrange(1,7)
diescore2 = random.randrange(1,7)

dieroll = diescore1 + diescore2

print('Dieroll', dieroll)

#  we can do this by a while loop

while(dieroll >= 8):

    diescore1 = random.randrange(1,7)
    diescore2 = random.randrange(1,7)
    dieroll = diescore1 + diescore2
        
    total = total + dieroll
    print('Dieroll = ', dieroll)
    print('Total = ', total)
print('Final Total = ', total)