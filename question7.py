#7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
color={'Id1':'Red','Id2':"Green",'Id3':'Blue'}
fruits={"F1":'Mango','F2':'Grapes','Id':'Apple'}
state={'S1':'Bhopal','S2':"Delhi",'S3':'Bihar'}
print(color,fruits,state,"\n\n")

India={'State':{'S1':'Bhopal','S2':"Delhi",'S3':'Bihar'},'fruits':{"F1":'Mango','F2':'Grapes','Id':'Apple'},'color':{'Id1':'Red','Id2':"Green",'Id3':'Blue'}}
print(India)
