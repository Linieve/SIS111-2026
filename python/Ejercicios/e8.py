"""
Una persona que va de compras a la multitienda "CyberSTORE" decide llevar 
un control sobre lo que va comprando, para saber la cantidad de dinero 
que tendrá que pagar al llegar a la caja
La tienda solamente vende 3 tipos de productos, estos pueden ser 
Televisores (codigo 1), Refrigeradores (codigo 2), Lavadoras (codigo 3)
No se puede ingresar el codigo de otro articulo, por lo que solo esos 3
valores pueden ser ingresados (validacion)
La persona comprará exactamente 3 articulos...

Ud. debe realizar un Algoritmo que permita, en cada uno de los 3 articulos:
    > Indicar el codigo
    > Ingresar la cantidad
    > Ingresar el valor unitario

Finalmente, el algoritmo debe dar como respuesta lo siguiente:

Se compraron X televisores, a un total de XXXXX
Se compraron Y refrigeradores, a un total de XXXXX
Se compraron Z lavadoras, a un total de XXXXX

"""

def validar(codigo):
    if codigo == 1 or codigo == 2 or codigo == 3:
        return True
    return False

def datos():
    lista[]
    for i in range(3):
        print("Seleccione su producto: \n Televisores (codigo 1), Refrigeradores (codigo 2), Lavadoras (codigo 3)")
        while True:
            codigo = int(input("Ingrese un codigo: "))
            if not validar(codigo):
                continue
            canti = int(input("Ingrese la cantidad de producto: "))
            valor = float(input("Ingrese el valor: "))
            bibli = {"codigo":codigo, "cantidad": canti, "valor": valor}
            lista.append(bibli)
            break
    return lista

def calcular():
    lista = datos()
    canti1=0
    canti2=0
    canti3=0
    valor1=0
    valor2=0
    valor3=0
    for i in range(len(lista)):
        if lista[i]["codigo"] == 1:
            canti1 = lsita[i]["cantidad"] + canti1
            valor1 = lista[i]["cantidad"]*lista[i]["valor"] + valor1
        else if lista[i]["codigo"] == 2:
            valor2 = lista[i]["cantidad"]*lista[i]["valor"] + valor2
            canti2 = lista[i]["cantidad"] + canti2
        else:
            valor3 = lista[i]["cantidad"]*lista[i]["valor"] + valor3
            canti3 = lista[i]["cantidad"] + canti3
def mostrar():
    print(f"Se compraron {canti1} de television con un valor total de {valor1}")
    print(f"Se compraron {canti2} de refrigerador con un valor total de {valor2}")
    print(f"Se compraron {canti3} de lavadora con un valor total de {valor3}")

mostrar()
    






