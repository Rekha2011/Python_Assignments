#Question 7:
#Here we have a list of 3 letters. I want you to concatenate this list with another list of numbers whose range varies from 1 to 3 (3 is included).
letters_list = ['H', 'R', 'S']
sample_list = ['{}{}'.format(lt_1,lt_2) for lt_2 in range(1, len(letters_list)+1) for lt_1 in letters_list]
print(sample_list)