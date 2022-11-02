from xml.sax.handler import EntityResolver


lista= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(len(lista))


def sarrus(lista):
    resultado = 0
    for i in range(3):
        resultado += lista[i%len(lista)][0]*lista[(i+1)%len(lista)][1]*lista[(i+2)%len(lista)][2]

    for i in range(3):
        resultado -= lista[i%len(lista)][0]*lista[(i+1)%len(lista)][1]*lista[(i+2)%len(lista)][2]
    return resultado


print(sarrus(lista))


