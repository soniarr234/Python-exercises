"""
Considera una lista/array de ovejas. Cada oveja tiene un nombre y un color. Haz una función que devuelva una lista con todas las ovejas que sean de color rojo y que además su nombre contenga tanto las letras n Y a, sin importar el orden, las mayúsculas o espacios.
Por ejemplo, si tenemos las ovejas:

const ovejas = [
  { name: 'Noa', color: 'azul' },
  { name: 'Euge', color: 'rojo' },
  { name: 'Navidad', color: 'rojo' },
  { name: 'Ki Na Ma', color: 'rojo'},
  { name: 'AAAAAaaaaa', color: 'rojo' },
  { name: 'Nnnnnnnn', color: 'rojo'}
]

Al ejecutar el método debería devolver lo siguiente:
// [{ name: 'Navidad', color: 'rojo' },
//  { name: 'Ki Na Ma', color: 'rojo' }]
Recuerda. Debe contener las dos letras 'a' y 'n' en el nombre. No cuentes ovejas que sólo tenga una de las letras, debe tener ambas.
"""

def filterSheep(sheeps):
  filtered_sheeps = []
  for sheep in sheeps:
    if sheep["color"] == "red":
      has_n = False
      has_a = False
      for char in sheep["name"].lower():
        if char == "a":
          has_a = True
        if char == "n":
          has_n = True
      if has_n and has_a:
        filtered_sheeps.append({"name": sheep ["name"], "color": sheep["color"]})
  
  return filtered_sheeps


sheeps = [
  {"name": "Noa", "color": "blue"},
  {"name": "Euge", "color": "red"},
  {"name": "Navidad", "color": "red"},
  {"name": "Ki Na Ma", "color": "red"},
  {"name": "AAAAAaaaaa", "color": "red"},
  {"name": "Nnnnnnnn", "color": "red"}
]
print(filterSheep(sheeps))
