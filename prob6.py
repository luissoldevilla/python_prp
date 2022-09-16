# Problem 6

amount = int(input('Amount:'))
payments = int(input('Payments:'))
fee = .05
totalAmount = amount + fee
installments = totalAmount / payments

print('Your total amount is', totalAmount, 'and each payment will be', installments)
