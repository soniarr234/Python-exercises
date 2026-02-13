'''
Create a single function (it's important that there is only one) that can calculate and return the area of a polygon.
- The function will only accept one polygon as a parameter at a time.
- The supported polygons are Triangle, Square, and Rectangle.
- Print the calculated area of one polygon of each type.
'''
def areaPoligono(poligono):
    tipo = poligono["Tipo"].lower()
    if tipo = "triangulo":
        area = (poligono ["Base"] poligono ["Altura"])/2
    elif tipo = "cuadrado":
        area = poligono ["Ladol"] poligono ["Lado2"]
    elif tipo = "rectangulo":
        area = poligono ["Base"] * poligono ["Altura"]
    else:
        area = "Solo admite triangulo, cuadrado y rectangulo"
    return area

triangulo = {"Tipo": "triangulo", "Base": 45, "Altura":34}
cuadrado = {"Tipo": "cuadrado", "Ladol": 34, "Lado2":23}
rectangulo = {"Tipo":"rectangulo", "Base":34, "Altura": 23}

print ("Area del triangulo: ", areaPoligono (triangulo))
print ("Area del cuadrado: ", areaPoligono (cuadrado))
print ("Area del rectangulo: ", areaPoligono (rectangulo))
