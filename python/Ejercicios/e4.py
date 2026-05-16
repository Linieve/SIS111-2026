#Escribir un algoritmo q calcule el area y volumen de un cilindro
#Ingrese el radio
#Area = (2*(PI*r^2)) + ((2*PI*r)*h)
#Volumen = (Pi*r^2)*h
import math
def ingresardatos():
    radio = float(input("radio:"))
    altura = float(input("altura:"))
    return (radio,altura)
def area(r, h):
    return (2*(math.pi*r*r)) + ((2*math.pi*r)*h)
def volumen(r, h):
    return (math.pi*r*r)*h
def mostrar():
    (r,h)=ingresardatos()
    print(f"la area es: {area(r,h)}")
    print(f"el volumen es: {volumen(r,h)}")
mostrar()