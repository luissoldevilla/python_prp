# Write a statement that creates a dictionary 
# containing the following key-value pairs:
dic = {'a':1,'b':2,'c':3}
print(dic)

# Write a statement that creates an empty dictionary.
dic2 = {}
print(dic2)

# Assume the variable dct references a dictionary. 
# Write an if statement that determines whether the key 'James' exists in the dictionary. 
# If so, display the value that is associ- ated with that key. 
# If the key is not in the dictionary, display a message indicating so.

if 'James' in dic:
    print(dic['James'])
else:
    print("James Not found")

# Assume the variable dct references a dictionary. 
# Write an if statement that determines whether the key 'Jim' exists in the dictionary. 
# If so, delete 'Jim' and its associated value.

if 'Jim' in dic:
    del dic['Jim']
    print(dic)
    print('Jim has been deleted')

else:
    print(dic)

# Write code to create a set with the 
# following integers as members: 10, 20, 30, and 40.

myset = set([10, 20, 30, 40])
