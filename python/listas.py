def bubblesort(lista,ascentende):
    cantidad = len(lista)
    for i in range(cantidad - 1):
        for j in range(cantidad-i-1):
            aux=0
            if(ascentende):
                if(lista[j]>lista[j+1]):
                    aux = lista[j]
                    lista[j]=lista[j+1]
                    lista[j+1]=aux
            else:
                if(lista[j]<lista[j+1]):
                    aux = lista[j]
                    lista[j]=lista[j+1]
                    lista[j+1]=aux
    return lista




lista = [7, 12, 9, 11, 3]
tupla = (7, 12, 9, 11, 3)       
print(bubblesort(lista,True))
print(bubblesort(lista,False))