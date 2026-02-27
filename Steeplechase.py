"""
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
 - La función recibirá dos parámetros:
      - Un array que sólo puede contener String con las palabras "run" o "jump"
      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 - La función imprimirá cómo ha finalizado la carrera:
      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
      - Si hace "run" en "|" (valla), se variará la pista por "/".
 - La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""
def steeplechase (steps, track):
  #I transform the string into an array to handle easier
  new_track = []
  for i in range(len(track)):
    new_track.append(track[i])
  
  isokay = True
  for i in range(len(new_track)):
    if new_track[i] == "_" and steps[i] == "jump":
      new_track[i] = "x"
      isokay=False
    elif new_track[i] == "|" and steps[i] == "run":
      new_track[i] = "/"
      isokay=False
  
  if isokay:
    print("You have passed the race", new_track)
    return True
  else:
    print("You have not passed the race", new_track)
    return False


steps =["jump", "run", "jump", "run", "jump", "run"]
track = "__|_|_"
print (steeplechase (steps, track))
