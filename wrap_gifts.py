"""
¡Hay demasiados regalos 🎁! Y envolverlos es una locura...

Vamos a crear una función que pasándole un array de regalos, nos devuelva otro array pero donde todos los regalos han sido envueltos con asteriscos tanto por arriba como por los lados.

Sólo tienes que tener en cuenta unas cosillas ✌️:

Si el array está vacío, devuelve un array vacío
Los regalos son emojis 🎁... por lo que tenlo en cuenta a la hora de contar su longitud...
Por suerte, cada posición del array siempre tiene la misma longitud...
wrapGifts(["📷", "⚽️"])
/* Resultado:
[ '****',
  '*📷*',
  '*⚽️*',
  '****'
]
*/

wrapGifts(["🏈🎸", "🎮🧸"])
/* Resultado:
[ '******',
  '*🏈🎸*',
  '*🎮🧸*',
  '******'
]
*/

wrapGifts(["📷"])
/* Resultado:
[ '****',
  '*📷*',
  '****'
]
*/
"""


def wrapGifts(list_gifts):
  list_wrap_gifts = []
  if len(list_gifts) == 0:
    return list_wrap_gifts

  len_gift = len(list_gifts[0])

  list_wrap_gifts.append("* " * (len_gift + 2))
               
  for gift in list_gifts:
    list_wrap_gifts.append("* " + gift + " *")

  list_wrap_gifts.append("* " * (len_gift + 2))

  return list_wrap_gifts

list_gifts = ["⚽️🏆", "🏐🥊"]
wrapped = wrapGifts(list_gifts)
for row in wrapped:
  print(row)
     
