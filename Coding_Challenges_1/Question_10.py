#Question 10:
#Given below is the height (in cm) of the top 10 students in a class. Print the heights of the top 3 students from the given list.
heights = [177, 160, 171, 163, 168, 175, 176, 183, 162, 170]
empty_lst = []
num = 3
for i in range(0, num):
    largeNo = 0
    for j in range(len(heights)):
        if heights[j] > largeNo:
            largeNo = heights[j]
    heights.remove(largeNo)
    empty_lst.append(largeNo)
print("Top Three Heights: ",empty_lst)