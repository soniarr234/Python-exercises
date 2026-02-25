"""
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
"""
def isAnagram (str1, str2):
    array_str1 = list(str1.lower())
    array_str2 = list(str2.lower())

    if len (array_str1) != len(array_str2):
        print ("It not an anagram")
        return False

    #It an anagram
    array_str1.sort()
    array_str2.sort()

    if array_str1 == array_str2:
        print ("It an anagram")
        return True
    else:
        print ("It not an anagram")
        return False

print (isAnagram("amar", "roma"))
