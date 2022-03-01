#Question 7:
#Write a function to reverse a string if it's length is an even number. I think of the TypeError exception if a numeric value is passed inside the function call. But there might be other exceptions too that can occur while executing the program.
#So, wrap the function around a try-except block and handle the TypeError exception with the message 'Check the string.' For all other exceptions, print the message 'Something went wrong.'
Input_String = "Python"[::-1]
print(Input_String)
