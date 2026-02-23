def maquinaExpendedora (compra):
  productos = {
    1: "Bolsa de patatas",
    2: "Colacao",
    3: "Cocacola",
    4: "Sandwich",
    5: "Galletas de Oreo"
  }
  precios = {
    1: 100,
    2: 85,
    3: 90,
    4: 125,
    5: 200
  }
  pago = compra[0]
  tecla = compra[1]

  #Compruebo que meta las monedas válidas
  monedas_validas = [5,10,50,100,200]
  moneda_ok = True
  total_monedas = 0

  for moneda in pago:
    if moneda not in monedas_validas:
      moneda_ok = False
      break
    else:
      total_monedas += moneda

  if moneda_ok == False:
    print("Introduce monedas válidas")
    return pago
  
  devolucion = []
  #Compruebo si da a una tecla válida
  if tecla in productos:
    if total_monedas == precios[tecla]:
      print ("Has elegido -->", productos[tecla])
      return devolucion
    elif total_monedas < precios[tecla]:
      print ("No tienes suficiente dinero")
      return pago
    else:
      monedas_validas.sort(reverse=True)
      cambio = total_monedas - precios[tecla]
      for moneda in monedas_validas:
        while cambio >= moneda:
          devolucion.append(moneda)
          cambio -= moneda
      print ("Has elegido -->", productos[tecla])
      return devolucion
  else:
    print("Producto no disponible")


compra = [[100,50], 2]
print (maquinaExpendedora (compra))
