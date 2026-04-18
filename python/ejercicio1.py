#Un programa q en un rango de 1 - 100 aleatorios genere 2 listas
#cantidad n numeros aleratorios
#una de numeros pares y otro de impares
#debera mostrar el total de la suma de la lista de pares y de impares
import random
def general(limite):
    numerosRan = []
    for count in range(limite):
        numero = random.randint(1,100) 
        numerosRan.append(numero)
    par = []
    impar = []
    sp=0
    si=0
    for i in range(limite):
        if numerosRan[i]%2==0:
            par.append(numerosRan[i])
            sp+=numerosRan[i]
        else:
            impar.append(numerosRan[i])
            si+=numerosRan[i] 
    return (f"numeros randoms: {numerosRan}, \npares: {par},\nsuma de pares: {sp},\nimpares: {impar},\nsuma de impares: {si}")

li=int(input())
print(general(li))

