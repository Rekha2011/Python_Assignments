#Question 9:
#Write a program to reverse words in a string.
sample_text = "Python is a high-level and general-purpose programming language"

reverse_string = sample_text.split(' ')
reverse_words = " ".join(reversed(reverse_string))
print(reverse_words)