"""
Busca que palabras están repetidas y muestralas
"""

words = ["Hello", "Bye", "Hello", "What", "Hello", "Google", "Bye", "Hello"]
repeated_words = []

for i in range (len (words)):
  for j in range (i+1, len (words)):
    if words [i] == words [j]:
      if words[i] not in repeated_words:
        repeated_words.append(words [i])

print (repeated_words)
