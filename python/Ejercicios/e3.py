#Escribir un algoritmo q calcule el area de un triangulo

def area(base, altura):
    return base*altura/2
print("Ingrese la base y altura: ")
b = int(input())
a = int(input())
print(area(b,a))