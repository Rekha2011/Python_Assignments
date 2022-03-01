#Question 9:
#Here we have a poem by Walt Whitman. I want you to print this poem once again after removing all the vowels from them.
poem = "Centre of equal daughters, equal sons, All, all alike endeared, grown, ungrown, young or old, Strong, ample, fair, enduring, capable, rich, Perennial with the Earth, with Freedom, Law and Love, A grand, sane, towering, seated Mother, Chaired in the adamant of Time."
empty_poem = ""
vowels = ['a', 'e', 'i', 'o', 'u']
for remove_vowel in poem:
    if remove_vowel not in vowels:
        empty_poem += remove_vowel
print(empty_poem)
