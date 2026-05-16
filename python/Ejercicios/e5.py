"""
Escribir un algoritmo q dado un valor en bolivianos x
realizar la conversion a dolares y a euros ademas debe introducir
el tipo de cambbio de las divisas
"""

def cambio():
    d=float(input("Ingrese el tipo de cambio de dolar:"))
    e=float(input("Ingrese el tipo de cambio de euro:"))
    return(d,e)
def conversion():
    (d,e)=cambio()
    b=float(input("Ingrese los Bolivianos:"))
    c_d=b/d
    c_e=b/e
    return(c_d,c_e)
def mostrar():
    (d,e) = conversion()
    print(f"Tienes actualmente {d} dolares o {e} euros")
mostrar()
