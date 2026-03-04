"""
Crea una función que reciba un texto y muestre cada palabra en una línea, formando un marco rectangular de asteriscos.
- ¿Qué te parece el reto? Se vería así:
    **********
    * ¿Qué   *
    * te     *
    * parece *
    * el     *
    * reto?  *
    **********
"""
def wordFrame(sentence):
    #Store each word in an array
    words = []
    word = ""
    sentence += " "     #Add extra space
    for char in sentence:
        if char != " ":
            word += char
        else:
            words.append(word)
            word = ""


    max_len = 0
    for word in words:
        length = len(word)
        if max_len < length:
            max_len = length
    
    num_spaces = max_len + 4
    for i in range (max_len + 4):
        print("*", end="")
    print()
    for word in words:
        num_spaces = max_len - (len(word))
        print("* " + word, (" " * num_spaces) + " *")
    for i in range (max_len + 4):
        print("*", end="")


print(wordFrame("¿Qué te parece el reto?")
