"""
un alumno desea saber cual sera su promedio general en tres materias 
mas dificiles que cursa y cual sera el promedio que obtendra en cada una
de ellas,
estas materias se evaluan como se muestra a continuacion

1. programacion
examen 90%
2 tareas 10%

2. algebra lineal
examen 80%
2 tareas 20%

3. sistemas
examen 85%
2 tareas 15%
"""
def ingresar():
    examen_programacion = float(input("Examen de programacion: "))
    examen_alge = float(input("Examen de algebra lineal: "))
    examen_sis = float(input("Examen de sistemas: "))
    pra1_programacion = float(input("practica 1 de programacion: "))
    pra2_programacion = float(input("practica 2 de programacion: "))
    pra1_alge = float(input("practica 1 de algebra lineal: "))
    pra2_alge = float(input("practica 2 de algebra lineal: "))
    pra1_sis = float(input("practica 1 de sistemas: "))
    pra2_sis = float(input("practica 2 de sistemas: "))
    return(examen_programacion,examen_alge,examen_sis,pra1_programacion,pra2_programacion,pra1_alge,pra2_alge,pra1_sis,pra2_sis)
def notas():
    (examen_programacion,examen_alge,examen_sis,pra1_programacion,pra2_programacion,pra1_alge,pra2_alge,pra1_sis,pra2_sis) = ingresar()
    e_p=examen_programacion/100*90
    e_al=examen_alge/100*80
    e_si=examen_sis/100*85
    p_p=(pra1_programacion+pra2_programacion)/2/100*10
    p_a=(pra1_alge+pra2_alge)/2/100*20
    p_s=(pra1_sis+pra2_sis)/2/100*15
    nf = (e_p+e_al+e_si+p_p+p_a+p_s)/3
    return nf
def mostrar():
    nf = notas()
    print(f"Tienes promedio de {nf} puntos")
mostrar()
    
