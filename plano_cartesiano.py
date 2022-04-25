"""Programa para indicar el cuadrante en el plano cartesiano a partir de dos coordenadas (x,y)"""

print("----------------------------------------------")
print("----- PLANO CARTESIANO COORDENADAS (x,y) -----")
print("----------------------------------------------")

# input
x=input("Digite el valor de x: ")
x=int (x)
y=input("Digite el valor de y: ")
y=int (y)

# processing
if x >= 1 and y >= 1:
    z = "Cuadrante I"

elif x <= -1 and y >= 1:
    z = "Cuadrante II"

elif x <= -1 and y <= -1:
    z = "Cuadrante III"

elif x >= 1 and y <= -1:
    z = "Cuadrante IV"

elif x <= -1 or x >= 1 and y == 0:
    z = "Eje X"

elif x ==0 and y <= 0 or y >= 1:
    z = "Eje Y"

elif x == 0 and y == 0:
    z = "Origen"

else:
    z = "Ingrese los valores para x & y"

# output 
print(z)