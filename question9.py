#9. Write a python program to merge two python dictionaries into one dictionary.
color={'Id1':'Red','Id2':"Green",'Id3':'Blue'}
fruits={"F1":'Mango','F2':'Grapes','Id':'Apple'}
dict3=color.copy()
for key, value in fruits.items():
    dict3[key] = value
print(dict3)

