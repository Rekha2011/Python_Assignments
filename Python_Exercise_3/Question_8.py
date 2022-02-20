#Question 8:
#Print all the even numbers between -10 and 0.
start, end = -10, 0

# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")