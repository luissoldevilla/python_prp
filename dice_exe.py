# we expoprt the library random
import random

total = 0
dieroll = 0
diescore1 = 0
diescore2 = 0

diescore1 = random.randrange(1,7)
diescore2 = random.randrange(1,7)

dieroll = diescore1 + diescore2

#  we have different prints
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



def main():
# Create a list to hold the sales for each day.
sales = [0] * NUM_DAYS
print('Enter the sales for each day.')

# Get the sales for each day.
for index in range(len(sales)):
sales[index] = float(input(f'Day #{index + 1}: '))
# Display the values entered.
print('Here are the values you entered:')
for value in sales:
print(value)
# Call the main function.
if __name__ == '__main__':
main()