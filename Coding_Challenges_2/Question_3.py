#Question 3:
#Find out the number of letters and digits from the given alpha-numeric text.
sample_text = "Learning Journal 2020"
letters = digits = 0
for ltr_dig in sample_text:
    if ltr_dig.isalpha():
        letters += 1
    elif ltr_dig.isdigit():
        digits +=1
print("Number of Letters:"+ str(letters) + '\n' + "Number of Digits:" + str(digits))