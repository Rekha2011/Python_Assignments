#Question 8:
#We have a dictionary given below. Copy this dictionary into another dictionary 'replica,' and change
#the value of the key 103 to 'Sally' in the replica dictionary only. Finally, print both the dictionaries.

a_dictionary = {101:'Judy', 102:'Victor', 103:'Sam'}
a_dictionary.update({101:'Judy', 102:'Victor', 103:'Sally'})
print(a_dictionary)

student_details = {101:'Judy', 102:'Victor', 103:'Sam'}
student_details1 = student_details.update({101:'Judy', 102:'Victor', 103:'Sally'})
print(student_details1)
