# Problem 215 # 9
# We can start the ocean level at 0
ocean_level = 0
# We set a variable for the constant value of 1.6
level_raise = 1.6
# print('Year' , 1, 'ocean level is:', level_raise)

for i in range(1,26):
    ocean_level = ocean_level + level_raise
    # This where we print 
    print('Year' , i, 'ocean level is:', ocean_level)