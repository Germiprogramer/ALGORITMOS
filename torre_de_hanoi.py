from tkinter import N
from pila.pila_germiprogramer import Pila, apilar, desapilar, pasar_elemento, condicion_hanoi, Nodo, imprimir

def ToH(n , A, B, C):
    if n==1:
        print("Disk 1 from",A,"to",B)
        return 
    ToH(n-1, A, C, B)
    print("Disk",n,"from",A,"to",B)
    ToH(n-1, C, B, A)
          
ToH(3,'A','B','C')


def apilar_primera_torre(pila1, n):
    for i in range(n+1):
        apilar(pila1,i)


def torre_de_hanoi(n, pila1, pila2, pila3):
    if n==1:
        return 
    torre_de_hanoi(n-1, pila1, pila3, pila2)
    pasar_elemento(pila1, pila3)
    torre_de_hanoi(n-1, pila3, pila2, pila1)

def hanoi_completo(n, pila1, pila2, pila3):
    apilar_primera_torre(pila1, n)
    torre_de_hanoi(n, pila1, pila2, pila3)

p1 = Pila()
p2 = Pila()
p3 = Pila()

hanoi_completo(9, p1, p2, p3)

imprimir(p2)

