def ordenar(lis, ascentende=True):
    if ascentende:
        return sorted(lis)
    else:
        return sorted(lis,reverse = True)



def ordenar2(lis, ascentende=True):
    lis.sort()
    if ascentende:
        return lis
    else:
        lis.reverse()
        return lis

lis = [3,6,3,7,1]

print(ordenar2(lis,True))
print(ordenar2(lis,False))