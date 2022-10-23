tuition_increase = 0.03
tuition = 8000
years = 5

# This is for console display

print('tuition\tyears')
print('--------------------')
print(tuition, '\t', 0)

# This is our logic

for years in range (1, years + 1):
    tuition *= (1+tuition_increase)
    print(tuition, '\t', years)