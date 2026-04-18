a = int(input())
import random
pares = "pares: "
impares = "impares: "
for i in range (a):
    x = random.randint(1, 100)
    print(x)
    i+=1
    if(x%2==0):
        pares = pares + f"{x}, "
    else:
        impares = impares + f"{x}, "
print(pares)
print(impares)

