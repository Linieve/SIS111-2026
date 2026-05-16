"""
 Indroduzca dos numeros que tengan mas de 3 digitos y determine si son o no AMIGOS(Validar).
(un numero es amigo del otro cuanmdo la suma de sus digitos es igual a la suma de los digitos del otro numero)

Ejemplo: Si A=5321 Y b=271010 --> se despliega: "Son amigos"
""" 
def validar(n):
    if n>999:
        return True
    return False
def hacer():
    while True:
        a = int(input("Indroducir el primer numero: "))
        if not validar(a):
            continue
        break
    while True:
        b = int(input("Indroducir el segundo numero: "))
        if not validar(b):
            continue
        break
    c1=0
    c2=0
    while not a%10==a:
        c1+=a%10
        a=a//10
    c1+=a
    while not b%10==b:
        c2+=b%10
        b=b//10
    c2+=b
    if c1==c2:
        print("Son amigos")
    else:
        print("No son amigos")
hacer()
