"""
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 Ejemplo: Ana lleva al oso la avellana.
"""

def isPalindrome(sentence):
  sentence = sentence.lower()
  accents = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
    "ñ": "n", "ü": "u", " ": ""
  }
  
  #Create a new variable to store the sentente without spaces, punctuation marks accent marks
  clear_sentence = ""
  for char in sentence:
    if char in accents:
      clear_sentence += accents[char]
    else:
      clear_sentence += char
  
  #Create a variable to store the sentences backwards
  backwards_sentence = ""
  for char in clear_sentence[::-1]:
    backwards_sentence += char

  if backwards_sentence == clear_sentence:
    print("It is a palindrome")
    return True
  else:
    print("It is not a palindrome")
    return False


print(isPalindrome("Ana lleva al oso la avellana"))
