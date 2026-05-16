"""
1. Una empresa quiere saber cuanto casta de locomocion y alimentacion de todos sus trabajadores.
Se sabe qye la empresa tiene un total de n trabajadores y cada uno tiene distinetos suledo, sin embargo 
a todos se les paga los mismos porcentajes locomocion y movilizacion calculados de a cuerdo con el suldo de cada uno. 
El nono de locomocion es de un 14% del suoldo y el nono de alimentacion es de un 9% del sueldo

Usred debe realizar un algoritmo que permita por cada uno de los n trabajadores:

Ingresa el CI de cada Trabajador(es un entero)
Ingresar el suldo de cada uno, el sueldo no puede ser menor de 5000bs, sino se cumple esa comdicion debe volver a ingresar
A medida que se ingrese se vaya calculando y mostrando cuanto paga por cada trabajador en cada uno de los bonos(locomocion y alimentos)
Finalmente, cuando se ingresen todos se indique cuanto la empresa gasta

. se gosto en total XX por conceptos de locomocion
.....
"""

def validar(ci):
    if ci%1==0:
        return True
    return False

def vali(sueldo):
    if sueldo >=5000:
        return True
    return False
def hacer():
    n=int(input("Ingrese la cantidad de trabajadores: "))
    cl=0
    ca=0
    for i in range(n):
        while True:
            ci = float(input("Ingrese su CI (Tiene q ser un entero): "))
            if not validar(ci):
                continue
            while True:
                sueldo = float(input("Ingrese su sueldo que no puede ser menor a 5000bs: "))
                if not vali(sueldo):
                    continue
                else:
                    break
            loco = sueldo*14/100
            ali = sueldo*9/100
            cl=cl+loco
            ca = ca+ali
            print(f"Se gasto en este trabajador {loco} por conceptos de locomocion y {ali} por conceptos de alimentacion")
            break
    print(f"En total se gasto {cl} por conceptos de locomocion \nSe gasto {ca} por conceptos de alimentacion")

hacer()
