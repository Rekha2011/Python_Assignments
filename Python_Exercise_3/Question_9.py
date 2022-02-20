#Question 9:
#Reverse the integer given below.
n = 5623
rev = 0

while (n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)