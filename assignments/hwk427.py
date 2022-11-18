def main():
    num_months = 12
    rain=[0]*num_months
    print('Enter the rain for each month.')
    for index in range(len(rain)):
        rain[index] = float(input(f'month #{index + 1}: '))
    print('Here are the values you entered:')
    for value in rain:
        print(value)
    sum_numbers=sum(rain)
    print('Total rain for 12 months are ',sum_numbers)
    average=sum_numbers/12
    print('The average rainfall per month is ',average)
    print('The highest value is', max(rain))
    print('The lowest value is', min(rain))

if __name__ == '__main__':
    main()