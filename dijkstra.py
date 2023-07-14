import numpy as np
import time


class Graph():
    def __init__(self, dir=False):
        self._n_nodes = None
        self._list = None
        self._distances = None
        self._dir=dir
        
    def initialize_graph(self, n_nodes):
        self._n_nodes = n_nodes
        print("Creating adjacence list")
        self._list = {node:[] for node in range(1, self._n_nodes+1)}
            
    def add_edge(self, u, v, weight=1):
        print("Adding edge...({},{})".format(u,v))
        if self._dir:
            self._list[u].append((v, weight))
        else:
            self._list[u].append((v, weight))
            self._list[v].append((u, weight))

    def graph_from_gr(self, file):
        with open(file) as file:
            for linha in file:
                values = linha.split(" ")
                if values[0]=='p':
                    self.initialize_graph(n_nodes=int(values[2]))
                elif values[0]=='a':
                    self.add_edge(u=int(values[1]), v=int(values[2]), weight=int(values[3]))

    def dijkstra(self, initial_node):
        start_time = time.time()
        distances = {node: np.inf for node in self._list.keys()}
        distances[initial_node] = 0
        visited = set()
        while visited != set(distances):
            vertice_atual = None
            menor_distancia = np.inf
            for v in self._list.keys():
                if v not in visited and distances[v] < menor_distancia:
                    vertice_atual = v
                    menor_distancia = distances[v]
            print("Total visitados {} de {}".format(len(visited)+1, self._n_nodes))
            visited.add(vertice_atual)
            try:
                for neighbor in self._list[vertice_atual]:
                    if distances[vertice_atual] + neighbor[1] < distances[neighbor[0]]:
                        distances[neighbor[0]] = distances[vertice_atual] + neighbor[1]
            except:
                print("vertex without neighbor")
                break
        self._distances = distances
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Dijkstra time: {elapsed_time:.8f} seconds")
      

    def show_distances(self):
        print(self._distances)
                    

if __name__=="__main__":
    grafo = Graph(dir=True)
    
    #Exemplo toy1
    '''
    grafo.initialize_graph(10)
    grafo.add_edge(u=1, v=2, weight=60)
    grafo.add_edge(u=1, v=3, weight=54)
    grafo.add_edge(u=1, v=4, weight=42)
    grafo.add_edge(u=2, v=4, weight=71)
    grafo.add_edge(u=3, v=4, weight=56)
    grafo.add_edge(u=2, v=5, weight=29)
    grafo.add_edge(u=3, v=6, weight=67)
    grafo.add_edge(u=4, v=5, weight=52)
    grafo.add_edge(u=4, v=6, weight=26)
    grafo.add_edge(u=4, v=7, weight=87)
    grafo.add_edge(u=5, v=7, weight=20)
    grafo.add_edge(u=6, v=7, weight=70)
    grafo.add_edge(u=6, v=9, weight=73)
    grafo.add_edge(u=7, v=9, weight=59)
    grafo.add_edge(u=5, v=8, weight=25)
    grafo.add_edge(u=7, v=8, weight=36)
    grafo.add_edge(u=8, v=10, weight=25)
    grafo.add_edge(u=9, v=10, weight=26)
    grafo.add_edge(u=7, v=10, weight=32)
    '''
    grafo.graph_from_gr("USA-road-d.NY.gr")
    grafo.dijkstra(1)
    #grafo.show_distances()
  

    