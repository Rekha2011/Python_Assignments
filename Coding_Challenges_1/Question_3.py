#Question 3:
#We have a set and a dictionary given below. Print the set once again after adding the keys of the dictionary to the set. The order of the expected output may vary as it is a set.
mySet = {2, 4, 6}
myDict = {'A':'John', 'B':'Emma', 'C':'Sam'}

for k in myDict.keys():
    mySet.update(k)
print(mySet, '\n')
