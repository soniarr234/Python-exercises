"""
Find the words that are repeated in a sentence
"""

user_input = "Python is fun and Python is entertain.
words = []
word = ""

for char in user_input:
  if char == " ":
    words.append(word)
    word = ""
  word += char

words.append (word)
count = 0

for i in range(len(words)-1):
  for j in range(i+1, len(words)):
    if words[i] == words[j]:
      count += 1
      print (words[i], "->", words[j])

print(count)
