#Question 6:
#Write a Python program to find the day of the week for the date given below. Also, we don't know what errors we might encounter while executing the program. So, wrap the code inside a try-except block and handle the exceptions by printing the message 'Oops! An error occurred.'
#given_date = datetime(2010, 6, 12)

import datetime
import calendar

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

# Driver program
date = '12 06 2010'
print(findDay(date))
