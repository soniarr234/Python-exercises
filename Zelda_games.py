"""
¡Han anunciado un nuevo "The Legend of Zelda"!
Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
 - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
"""

from datetime import datetime

def zeldaGames(game1, game2):
  zelda_games_dic = {
    "The Legend of Zelda": "21/02/1986",
    "Zelda II: The Adventure of Link": "14/01/1987",
    "A Link to the Past": "21/11/1991",
    "Link's Awakening": "06/06/1993",
    "Ocarina of Time": "21/11/1998",
    "Majora's Mask": "27/04/2000",
    "Oracle of Seasons/Ages": "27/02/2001",
    "The Wind Waker": "13/12/2002",
    "Four Swords Adventures": "18/03/2004",
    "The Minish Cap": "04/11/2004",
    "Twilight Princess": "19/11/2006",
    "Phantom Hourglass": "23/06/2007",
    "Spirit Tracks": "07/12/2009",
    "Skyward Sword": "18/11/2011",
    "A Link Between Worlds": "22/11/2013",
    "Tri Force Heroes": "22/10/2015",
    "Breath of the Wild": "03/03/2017",
    "Tears of the Kingdom": "12/05/2023",
    "Echoes of Wisdom": "26/09/2024"
  }
  result = ""
  #Change string to date
  date1 = datetime.strptime(zelda_games_dic[game1], "%d/%m/%Y")
  date2 = datetime.strptime (zelda_games_dic[game2], "%d/%m/%Y")
  
  subtraction = date2 - date1
  days=subtraction.days
  years = days // 365
  remaining_days = days % 365
  if days < 0 or years < 0:
    result = f"The game: {game1} is newer than the game: {game2}"
  else:
    if years == 0:
      result = f"{days} days have passed"
    else:
      result = f"{years} year(s) and {remaining_days} day(s) have passed"
  
  return result


print(zeldaGames ("Tears of the Kingdom", "Echoes of Wisdom"))
