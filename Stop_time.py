"""
Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
  - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
  - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal.
 Se podría ejecutar varias veces al mismo tiempo.
"""
import asyncio
async def stopTime(num1, num2,  seg):
  await asyncio.sleep(seg)
  return num1 + num2

async def main():
  num1 = 5
  num2 = 3
  seg = 10
  result = await stopTime(num1, num2, seg)
  print(result)

asyncio.run(main())
