#Question 1:
#We have two lists of numbers given below. I want you to create a third list by picking an odd-indexed element from the first list and even-indexed elements from the second list.
list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]
third_list = []
for i in list_1:
    if i%2 == 0:
        third_list.append(i)
for j in list_2:
    if j%2 != 0:
        third_list.append(j)
print(str(third_list))
