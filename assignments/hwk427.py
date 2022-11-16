num_digits = 12

rainfall_amount = [0] * num_digits
print('Enter ....')

for index in range(len(rainfall_amount)):
    rainfall_amount[index] = int(input('Enter the amount of rainfall'))
    total = total + rainfall_amount[index]
for value in rainfall_amount:
    print(value)
print('The lowest value is', min(rainfall_amount))