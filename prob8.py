# Problam 8

food = int(input('Meal Cost:'))
tip = int(food * .18)
tax = food * .07

totalFood = food + tip + tax

print('Tip:', tip)
print('Tax', tax)
print('Your total bill is:', totalFood)