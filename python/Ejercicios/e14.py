"""
Obtenga la suma de numeros prinos conprendidos entre 2...n
Ejemplo:
n=10

Salida: 
Numeros primos: 2,3,5,7
Suma 17
"""

def cribal():
    n = int(input("Introduzca el numero n: "))
    lis=[]
    li=[1]*(n+1) #[0,0,1,1,0,1,0,1,0,0,0]
    li[0]=0
    li[1]=0
    c=0
    for i in range(2,n+1):
        if not li[i]==0:
            c+=i
            lis.append(i)
            for j in range(2,n+1):
                if j*i<=n:
                    li[j*i]=0
    print(f"Los primos son: {lis} y la suma es: {c}")

cribal()