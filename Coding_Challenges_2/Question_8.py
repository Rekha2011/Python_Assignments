#Question 8:
#Print all the numbers between 1 and 100 (both being included) that are multiples of 3 and 5 both.

both = [get_mul for get_mul in range(1, 100) if (get_mul%3 == 0) and (get_mul%5 == 0)]
print(both)