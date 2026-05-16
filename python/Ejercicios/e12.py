"""
Una persona se va de compras a la tienda "El diablo" decide llevar un control sobre lo que va comprando, 
para saber la cantidad de dinero que tendra que pagar al llegar a la caja. 
La tienda tiene una promocion del 20% (20/100) de descuento sobre aquellos articulos cuya etiqueta tenga el numero 666. 
Todos los articulos tienen etiqueta. La persona comprará exactamente n productos. Usted debe realizar un Algoritmo que permita ingresar:

El valor de cada producto 
El numero que aparece en la etiqueta. 
Estos numeros son entre 1 y 1000, no se permite ingresar otro numero fuera de este rango (Validar)

Recuerde que, el algoritmo debe aplicar el descuento al valor del producto cuando corresponda (los que tienen etiqueta 666)

Finalmente debe mostrar el total final de dinero que esta persona deberá pagar por el total de todos sus productos.
"""

def validar(eti):
    if eti>=1 and eti<=1000 and eti%1==0:
        return True
    return False

def hacer():
    c=0
    n = int(input("Ingrese la cantidad de productos de desea comprar: "))
    for i in range(n):
        while True:
            eti = float(input("Ingrese su etiqueta (entre 1 y 1000): "))
            if not validar(eti):
                continue
            pre = float(input("Ingrese su valor: "))
            if eti==666:
                pre=pre-pre*20/100
            c+=pre
            break
    return c

def mostrar():
    c=hacer()
    print(f"En total se gasto {c} Bolivianos")

mostrar()

