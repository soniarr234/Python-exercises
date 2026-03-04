"""
¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
  Cada raza tiene asociado un "valor" entre 1 y 5:
  - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
  - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
  Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
  - El resultado puede ser que gane el bien, el mal, o exista un empate.
    Dependiendo de la suma del valor del ejército y el número de integrantes.
  - Cada ejército puede estar compuesto por un número de integrantes variable
    de cada raza.
  - Tienes total libertad para modelar los datos del ejercicio.
  Ej: 1 Peloso pierde contra 1 Orco
      2 Pelosos empatan contra 1 Orco
      3 Pelosos ganan a 1 Orco
"""

def rignsPower(num_kind, kind, num_evil, evil):
    result = ""
    
    kind_dic = {
        "Pelosos": 1, "Sureños buenos": 2, "Enanos": 3, "Númenóreanos": 4, "Elfos": 5
    }
    evil_dic = {
        "Sureños malos": 2, "Orcos": 2, "Goblins": 2, "Huargos": 3, "Trolls": 5
    }
    
    total_kind = kind_dic[kind] * num_kind
    total_evil = evil_dic[evil] * num_evil
    if total_kind > total_evil:
        result = f"{num_kind} {kind} ganan a {num_evil} {evil}"
    elif total_kind < total_evil:
        result = f"{num_kind} {kind} pierden contra {num_evil} {evil}"
    else:
        result = f"{num_kind} {kind} empatan contra {num_evil} {evil}"

    return result


print (rignsPower(2, "Pelosos", 1, "Orcos"))
