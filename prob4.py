# Problem 4 # 
item1 = float(input('Enter value of item 1:'))
item2 = float(input('Enter value of item 2:'))
item3 = float(input('Enter value of item 3:'))
item4 = float(input('Enter value of item 4:'))
item5 = float(input('Enter value of item 5:'))

subtotal = item1 + item2 + item3 +item4 + item5

tax = subtotal * 0.07

total = subtotal + tax
print('Your subtotal is:', subtotal)
print('Total:', total)