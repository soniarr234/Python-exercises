'''
Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 - Paréntesis, llaves y corchetes son igual de prioritarios.
   No hay uno más importante que otro.
 - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 - Expresión no balanceada: { a * ( c + d ) ] - 5 }
'''

expression = "{ a * ( c + d   - 5 "
container = []
dic_symbols = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
}
last_symbol = ""
balanced_expression = True

for i in expression:
    #Si es alguno de esos simbolos, lo guardo en el array
    if i == "(" or i == "[" or i == "{":
        container.append(i)
    #Mirar que simbolo entró por última vez en el array y compararlo con el diccionario
    if i == ")" or i == "]" or i == "}":
        if len(container) == 0:
            balanced_expression = False
        else:
            last_symbol = container.pop()
            if dic_symbols[last_symbol] == i:
                balanced_expression = True
            else:
                balanced_expression = False
                break


if len(container) == 0 and balanced_expression:
    print("Balanced expression")
else:
    print("Unbalanced expression")
