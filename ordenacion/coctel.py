l = [2,1,4,3]

def comp_der(a,b):
    return a == b
    

comp_der(l[1],l[2])

print(l)


def coctel(lista):
    izquierda = 0
    derecha = len(lista)-1
    control = True

    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if (lista[i] > lista[i+1]):
                control = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
        derecha = -1
        for j in range(derecha,izquierda,-1):
            if (lista[j]<lista[j-1]):
                control = True
                lista[j], lista[j-1] = lista[j-1], lista[j]
        izquierda +=1

