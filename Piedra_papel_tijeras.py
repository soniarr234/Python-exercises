"""
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
  - El resultado puede ser: "Jugador 1", "Jugador 2", "Empate"
  - Ejemplo. Entrada: [("Piedra","Tijeras"), ("Tijeras","Piedra"), ("Papel","Tijeras")].
    Resultado: "Jugador 2"
"""

jugadas = [("Piedra", "Tijeras"), ("Tijeras", "Piedra"),("Papel","Tijeras")]
contador_jugador1 = 0
contador_jugador2 = 0
contador empate = 0

reglas = {
  ("Piedra", "Tijeras"): "1",
  ("Papel", "Piedra"): "1",
  ("Tijeras", "Papel"): "1",
  
  ("Piedra", "Papel"): "2",
  ("Tijeras", "Piedra"): "2",
  ("Papel", "Tijeras"): "2",
  
  ("Piedra", "Piedra"): "0",
  ("Tijeras", "Tijeras"): "0",
  ("Papel", "Papel"): "0",
}

for jugada in jugadas:
  if reglas[jugada] == "1":
    contador_jugador1 += 1
  elif reglas[jugada] == "2":
    contador_jugador2 += 1
  else:
    contador_empate += 1

if contador_jugador1 > contador_jugador2:
  print ("Ha ganado el jugador 1")
elif contador_jugador1 < contador_jugador2:
  print ("Ha ganado el jugador 2")
else:
  print ("Han quedado empate")
