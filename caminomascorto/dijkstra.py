import sys
#________________________________________________________
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = init_graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        
        for out_node in self.nodes:
                if self.graph[node].get(out_node, False) != False:
                    connections.append(out_node)
        
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]
#___________________________________________________________________

	
def dijkstra_algorithm(graph, start_node):
    #graph viene de construct graph, start node es el nodo donde empezamos

    #creamos una lista de los nodos no visitados
    unvisited_nodes = list(graph.get_nodes())

    shortest_path = {}
    previous_nodes = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0

    #el algoritmo se acaba cuando todos los nodos han sido visitados
    while unvisited_nodes != None:
        current_min_node = None
        #iterar en los nodos
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
            #el algoritmo visita todos los vecinos del nodo que no han sido vistados
        #corrige el camino por si no estabamos yendo por el camino más corto
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)
        
    return previous_nodes, shortest_path
#___________________________________________________________________________________-
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

#_______________________________________________________________________________________
nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}

def añadir_elemento(grafo, nodo1, nodo2, distancia):
      grafo[nodo1][nodo2] = distancia
      grafo[nodo2][nodo1] = distancia


init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2


#___________________________________________________________________________________________________________
graph = Graph(nodes, init_graph)


previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")

print_result(previous_nodes, shortest_path, "Reykjavik", "Belgrade")