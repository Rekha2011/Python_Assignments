#Question 10:
#Write a program to process the results of the user. The program should consist of a user-defined exception class 'InvalidNumError' to raise an error if the marks entered by the user is less than 0 or greater than 100. Otherwise, print the message 'Results processing.'

num = float(input("100"))
if num > 0:
   print("Error! Try again.")

else:
   print("Results processing")