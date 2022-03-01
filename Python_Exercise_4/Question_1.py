#Question 1:
#We have two sets given below. Print the set of elements that are present in either set1 or set2 but
#not both.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set1.symmetric_difference_update(set2)
print(set1)