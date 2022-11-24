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