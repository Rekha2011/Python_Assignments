#Question 4:
#We have a dictionary given below. Delete the item with key '3,' and add an item with key '7' and
#value 'Black.'
myDict = {1:'Red', 2:'Orange', 3:'White', 4:'Brown', 5:'Yellow'}

myDict.pop(3, 'White')
myDict.get(7, 'Black')
print(myDict)