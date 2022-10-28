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

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
init_graph = {}
for node in nodes:
    init_graph[node] = {}
def añadir_elemento(grafo, nodo1, nodo2, distancia):
      grafo[nodo1][nodo2] = distancia
      grafo[nodo2][nodo1] = distancia

añadir_elemento(init_graph, "Reykjavik", "Oslo", 5)
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2

print(init_graph)