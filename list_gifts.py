def listGifts(letter):
  gifts = []
  gift = ""
  letter += " "
  for char in letter:
    if char == " ":
      if gift != "":
        gifts.append(gift)
        gift = ""
      else:
        gift = ""
    else:
      gift += char

  valid_gifts = {}
  for gift in gifts:
    if gift[0] != "_":
      if gift not in valid_gifts:
        valid_gifts[gift] = 1
      else:
        valid_gifts[gift] += 1
  return valid_gifts


letter = "bici coche balon _playstation bici coche peluche"
print(listGifts(letter))
