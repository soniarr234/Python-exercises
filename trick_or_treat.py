"""
Este es un reto especial por Halloween.
Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y un listado (array) de personas con las siguientes propiedades:
 - Nombre de la niña o niño
 - Edad
 - Altura en centímetros

Si las personas han pedido truco, el programa retornará sustos (aleatorios) siguiendo estos criterios:
 - Un susto por cada 2 letras del nombre por persona
 - Dos sustos por cada edad que sea un número par
 - Tres sustos por cada 100 cm de altura entre todas las personas
 - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 
 Si las personas han pedido trato, el programa retornará dulces (aleatorios) siguiendo estos criterios:
 - Un dulce por cada letra de nombre
 - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 - En caso contrario retornará un error.
"""

import random

def trickTreat(people, choiseTrickOrTreat):
    scares = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
    sweets = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
    results_trick = []
    results_treat = []

    names = ""
    total_height = 0

    #People choose Trick
    for person in people:
        #NAMES
        if choiseTrickOrTreat == "Trick":
            names = person["name"]
            for i in range(1, len(names), 2):
                results_trick += random.choice(scares)

            #AGES
            ages = person["age"]
            if ages % 2 == 0:
                results_trick += random.sample(scares, 2)

            #HEIGHT
            height = person["height"]
            total_height += height

        if choiseTrickOrTreat == "Treat":
            # NAMES
            names = person["name"]
            for i in range(len(names)):
                results_treat += random.choice(sweets)

            # AGES
            age = person["age"]
            limit = age
            if limit > 10:
                limit = 10
            for i in range(3, limit + 1, 3):
                results_treat += random.choice(sweets)

            # HEIGHT
            height = person["height"]
            limit = height
            if limit > 150:
                limit = 150
            for i in range(50, limit + 1, 50):
                results_treat += random.sample(sweets, 2)

    if choiseTrickOrTreat == "Trick":
        #Recorrer la altura total de todos de 100 en 100
        for i in range(100, total_height, 100):
            results_trick += random.sample(scares, 3)
        return results_trick
    elif choiseTrickOrTreat == "Treat":
        return results_treat


people = [
    {"name": "Sonia", "age": 28, "height": 175},
    {"name": "Irene", "age": 22, "height": 162},
    {"name": "Ron", "age": 3, "height": 15}
]
choiseTrickOrTreat = "Treat"

print(trickTreat(people, choiseTrickOrTreat))
