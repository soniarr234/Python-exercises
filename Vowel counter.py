"""
Asks the user to enter a word or sentence.
Counts how many vowels (a, e, i, o, u) appear in the text.
Ignores uppercase and lowercase differences (for example, A and a should be treated as the same).
Prints the total number of vowels found.
"""

user_input = input ("Enter a wold or sentence")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count_vowel = 0

for i in user_input:
  for vowel in vowels:
    if i == vowel:
      count_vowel += 1

if count_vowel > 0:
  print ("There are", count_vowel)
else:
  print ("There aren't vowels")
