#Question 8:
#Using the slicing operation, remove the whitespaces between the letters and print the string once
#again.
name = 'P y t h o n'
def remove(name):
    return "".join(name.split())
name = 'P y t h o n'
print(remove(name))