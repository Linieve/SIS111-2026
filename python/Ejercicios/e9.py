def validar(codigo):
    if codigo == 1 or codigo == 2 or codigo == 3:
        return True
    return False

def ingresar():
    n = int(input("Ingrese la cantidad de trabajadores: "))
    c1=0 
    c2=0
    c3=0
    v1=0
    v2=0
    v3=0
    for i in range(n):
        while True:
            print("Seleccione su estado Civil: \n Soltero (codigo 1), Casadas (codigo 2), En pareja (codigo 3)")
            codi = int(input(""))
            if not validar(codi):
                continue
            hijo = int(input("Ingrese la cantidad de hijos que tiene: "))
            if codi == 1:
                c1+=hijo
                v1+=1
            elif codi == 2:
                c2 += hijo
                v2+=1
            else:
                c3 += hijo
                v3+=1
            break
    return (c1,c2,c3,v1,v2,v3)

def mostrar():
    (c1,c2,c3,v1,v2,v3) = ingresar()
    print(f"Hay {v1} trabajadores Solteros, con {c1} hijos")
    print(f"Hay {v2} trabajadores Casados, con {c2} hijos")
    print(f"Hay {v3} trabajadores En pareja, con {c3} hijos")
    print(f"El bono total es {(c1+c2+c3)*2000} Bolivianos")

mostrar()