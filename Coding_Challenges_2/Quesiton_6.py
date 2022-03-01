#Question 6:
#Print all the prime numbers between the given range.
start = 20
end = 60
print("Prime numbers between 20 and 60 are:", end='')
for num in range(start, end+1):
    if num>1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)