#Elaborar un algoritmo dado un numero limite = n de aleatorios entre 1 y 100, encontrar las coincidencias de x
import random
"""
a = int(input())
n=[0] *101
for i in range(a):
    x = random.randint(1, 100)
    print(x)
    n[x]=n[x]+1

y = int(input())
print(n[y])
"""
def general(limite):
    numerosRan = []
    for count in range(limite):
        numero = random.randint(1,100)
        numerosRan.append(numero)
    return numerosRan

def buscar(x,limite):
    c = 0
    aleatorios = general(limite)
    for numero in aleatorios:
        if numero ==x:
            c+=1
    return (f"Numero de coincidencia para {x} es de: {c}")

a= int(input())
b= int(input())
print(buscar(b,a))
print(general(a))

