print("Indroduzca tres numeros: ")
a = int(input())
b = int(input())
c = int(input())

if a>b and a>c:
    print(a, "es el mayor")
    if b<c:
        print(b, "es el menor")
    else:
        print(c, "es el menor")
elif a>b:
    print(c, "es el mayor")
    print(b, "es el menor")
elif a>c:
    print(b, "es el mayor")
    print(c, "es el menor")
else:
    if b>c:
        print(b, "es el mayor")
    else:
        print(c, "es el mayor")
    print(a, "es el menor")