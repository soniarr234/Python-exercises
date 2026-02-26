"""
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 - Los signos de puntuación no forman parte de la palabra.
 - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

sentence = "Carmen, ¿que tal esta carmen tu hija Carmen?, adios Hija"
sentence = sentence.lower()
sentence += " "
invalid_char = ["¿", "?", "!", "¡", ";", ".", ":", ";", ","]
words = []
word = ""

#Separate the words and put them in a words array
for char in sentence:
#Delete the invalid character
  if char in invalid_char:
    continue
  
  if char != " ":
    word += char
  else:
    words.append(word)
    word = ""

#Create a dictionary to store the words and how many time each one appears
dict_word ={}
for i in range (len (words)):
  if words[i] not in dict_word:
    dict_word[words[i]] = 1
  else:
    dict_word[words[i]] += 1
    
print(dict_word)
