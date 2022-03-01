#Question 7:
#We have a list of lists that contains several numbers. I want you to print the list whose sum of elements is the highest and also the lowest.
num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]

print("The list with the maximum sum of elements: ",max(num_list, key=sum))
print("The list with the minimum sum of elements: ",min(num_list, key=sum),'\n')