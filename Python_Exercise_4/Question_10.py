#Question 10:
#Print the number and the cube of that number in a dictionary from 0 to 5.
# Initializing list
cube_list = [0, 1, 2, 3, 4, 5]

# Cube List using list comprehension
cube1 = [pow(i, 3) for i in cube_list]

# printing result
print(cube1)