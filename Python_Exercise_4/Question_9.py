#Question 9:
#Remove all the duplicate items from the tuple given below.
myTuple = ('Red', 'Blue', 'Green', 'Red', 'Orange', 'Green')

dup_tup = tuple(set(myTuple))

# printing result
print(dup_tup)