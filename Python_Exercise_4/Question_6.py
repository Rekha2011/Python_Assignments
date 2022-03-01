#Question 6:
#Merge the two dictionaries given below.
myDict1 = {1:'One', 2:'Two', 3:'Three'}
myDict2 = {4:'Four', 5:'Five', 6:'Six'}

merge = myDict1.copy()
merge.update(myDict2)
print(merge)