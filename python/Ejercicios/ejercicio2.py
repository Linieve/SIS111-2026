#Crear un programa en python o typscript que muestre un menu interativo con las siguientes opciones:
# 1 suamr numeros
# 2 restar numeros
# 3 multiplicar numeros
# 4 dividir numeros
# 5 salir
# el usuario debe poder elegir una opcion del menu y luego introducir numeros 
# el programa debe mostrar el resultado y volver a mostrar el menu hasta q el usuaria elija 5
# Si el usuario elije una opcion invalida, el programa debe mostrar una opcion de error

def hacer(lista, op):
    s = 0
    r = lista[0]*2
    m = 1
    d = lista[0]**2
    for i in range(len(lista)):
        s+=lista[i]
        r-=lista[i]
        m*=lista[i]
        d/=lista[i]
    if op==1:
        return f"La suma sale: {s}\n"
    elif op == 2:
        return f"La resta sale: {r}\n"
    elif op == 3:
        return f"La multiplicacion sale: {m}\n" 
    elif op == 4:
        return f"La division sale: {d} \n"
    elif op == 5:
        return ""
    else:
        return "ERROR"


op=0
while True:
    lista = []
    print("Introcuci el tipo de operación:\n1=suma \n2=resta \n3=multiplicacion \n4=division\n5=salir ")
    op = int(input())
    if op == 5:
        break
    elif op !=1 and op !=2 and op!=3 and op!=4:
        print("Error")
        break
    print("Introduci con cuantos numeros quiere trabajar: ")
    n = int(input())
    print("Introduzca los numeros: ")
    while n!=0:
        a = int(input())
        lista.append(a)
        n-=1
    print(hacer(lista,op))


