#Question 9:
#Write a program to square the number entered by the user. But what if the user enters a string or an alphanumeric value, or if some other unexpected exceptions occur. So, wrap the program inside the try-except block to handle the exceptions, and the program should run until the user enters a numeric value.

print("Enter a number aa")
# input a number
digit = int(input("Enter an integer number: 10"))

# calculate square
square = digit*digit

# print
print(f"Square of {digit} is {square}")