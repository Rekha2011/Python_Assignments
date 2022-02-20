#Question 8:
#We have a number given below. Write a program to check for the divisibility of this number by 3 and
#5, and print the result obtained.
a = 12
num1 = int(input("3"))
num2 = int(input("5"))
# checking divisibilty.
if num1%num2==0:
  print("\n" +str(num1)+ "is divisible by" +str(num2))
else:
  print("\n" +str(num1)+ "is not divisible by" +str(num2))