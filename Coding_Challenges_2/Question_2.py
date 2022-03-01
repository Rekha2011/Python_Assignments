#Question 2:
#You have two dictionaries, with each of them containing several letters associated with certain values.
num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}

print("1." + '\n' + str(set(num_1).intersection(set(num_2))) +'\n')
print("2.")
empty_dict = dict()
for k,v in num_1.items():
    # to checks the common values from two dictionary's
    if k in num_2 and num_1[k] == num_2[k]:
        empty_dict[k] = num_1[k]
print(str(empty_dict))
print("3." + str(set(num_1).union(set(num_2))))
print("4." + str(set(num_1).difference(set(num_2))))
print("5.")
num_3 = dict()
for key, value in num_1.items():
    if key not in num_2:
        num_3[key] = value
print(str(num_3))