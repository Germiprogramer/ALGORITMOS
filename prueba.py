import random

lista2 = []
for i in range(5):
    lista2.append([])
    for j in range(5):
        lista2[i].append(random.randint(0,1))	

print(lista2)


laberinto = [
    [0,1,1,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [1,0,0,0,0]
]


