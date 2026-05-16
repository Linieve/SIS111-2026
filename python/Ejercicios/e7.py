def ingresar():
    lista=[]
    asignatura = []
    ma = int(input("Ingrese la cantidad de asignaturas: ")) 
    for i in range(ma):
        nombre = input("Nombre de la asignatura: ")
        asignatura.append(nombre)
        exa = int(input(f"Ingrese la cantidad de examen del {nombre}: "))
        pra = int(input(f"Ingrese la cantidad de practica del {nombre}: "))
        puex = float(input(f"Ingrese el porcentaje de caliificacon de examen de {nombre}: "))
        pupra = 100 - puex
        contador_examen = 0
        contador_practicas = 0
        for j in range(exa):
            a = float(input(f"Ingrese el {j+1} nota del examen del {nombre}: "))
            contador_examen += a
        puntos_examen = contador_examen/exa/100*puex
        for j in range(pra):
            a = float(input(f"Ingrese el {j+1} nota de la practica del {nombre}: "))
            contador_practicas += a
        puntos_practica = contador_practicas/pra/100*pupra
        nota_final = puntos_examen + puntos_practica
        lista.append(nota_final)
    return (lista,ma,asignatura)

def mostrar():
    (lista,ma,asignatura) = ingresar()
    for i in range(len(lista)):
        print(f"El promedio de {asignatura[i]} es {lista[i]}")
            
mostrar()