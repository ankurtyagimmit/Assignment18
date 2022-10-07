'''#8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
list1=['python',22,45,'Java']
list2=['Hindi','English','Math','Computer']
dictionary={"['python',22,45,'Java']":"['Hindi','English','Math','Computer']"}
print(dictionary)'''
# Defining a Python list
ls = ['E', 69, 'J', 74, 'O', 79, 'T', 84, 'Y', 89]
 
# Creating an iterator for list 'ls'
item = iter(ls)
 
# Using the Python zip() function to convert the list to a dictionary
ds = dict(zip(item, item))
 
# Printing the results
print("Given Python list: ", ls)
print("Generated Python dictionary: ", ds)
 
# Validating the type of 'ds'
print(type(ds))
