#Question 7:
#Check if the cities 'New York' and 'Delhi' are present in the list of cities given below.
cityList = ['London', 'New York', 'Delhi', 'Mumbai', 'Paris']
result = {'New York': True}
cityList1 = ['London', 'New York', 'Delhi', 'Mumbai', 'Paris']
result = {'Delhi': True}
print(all(cityList))
print(all(cityList1))