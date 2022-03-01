#We have a function given below that adds elements of two lists. However, I can think of two exceptions that can occur in this program.
#The index entered by the user during the function call may be out of bound.
#The list entered by the user can consist of int objects, str objects, or even a combination of both. And what if we try to add an int object and an str object?
#Re-write this program to handle the two exceptions mentioned above.

color = ['red', 'blue', 'green', 'pink']
color1 = ['black', 'white']
color1.append(color)
print(color1[len(color1)])

