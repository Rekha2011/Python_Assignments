#Question 9:
#Write a Python program to check if the given year is a leap year.


year = int(input('1996'))

if (Year % 4) == 0:
       if (Year % 400) == 0:
           print("{0} is a leap year".format(Year))
       else:
           print("{0} is not a leap year".format(Year))

print("Leap Year")