import numpy as np
import time
import heapq


class Graph():
    def __init__(self, dir):
        self._n_nodes = None
        self._list = None
        self._distances = None
        self._sets = None
        self._dir = dir
        
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

    def find_set(self, v):
        for s in self._sets:
            if v in self._sets[s]:
                return s
               
    def kruskal(self):
        start_time = time.time()
        edges = []
        for u in self._list:
            for v, weight in self._list[u]:
                #edges.append((weight, u, v))
                heapq.heappush(edges, (weight, u, v))
        #edges.sort()        
        num_vertices = len(list(self._list.keys()))
        mst = []
        self._sets = {v: {v} for v in self._list}
        i = 0
        while edges:
            weight, u, v = heapq.heappop(edges)
            print("Getting edge {} of {} edges".format(i, len(edges)))
            i +=1
            set_u = self.find_set(u)
            set_v = self.find_set(v)

            if set_u != set_v:
                mst.append((u, v, weight))
                self._sets[set_u].update(self._sets[set_v])

                for vertex in self._sets[set_v]:
                    self._sets[vertex] = self._sets[set_u]
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Kruskal time: {elapsed_time:.8f} seconds")
        return mst      

        

    def show_distances(self):
        print(self._distances)
                    

if __name__=="__main__":
    grafo = Graph(dir=True)
    
    #Exemplo toy1
    
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
    
    #EXEMPLO TOY2
    '''
    grafo.initialize_graph(6)
    grafo.add_edge(u=1, v=2, weight=1)
    grafo.add_edge(u=1, v=3, weight=3)
    grafo.add_edge(u=2, v=3, weight=1)
    grafo.add_edge(u=2, v=5, weight=2)
    grafo.add_edge(u=2, v=4, weight=3)
    grafo.add_edge(u=3, v=4, weight=2)
    grafo.add_edge(u=5, v=4, weight=-3)
    grafo.add_edge(u=4, v=5, weight=-1)
    grafo.add_edge(u=4, v=6, weight=2)
    grafo.add_edge(u=6, v=5, weight=3)
    '''
    grafo.graph_from_gr("/home/jaimel/Downloads/USA-road-d.NY.gr")
    mst = grafo.kruskal()
    total = 0
    #print(mst)
    for aresta in mst:
        total += aresta[2]
    print(total)
    #grafo.dijkstra(1)
    #grafo.show_distances()
    #mst = grafo.kruskal()
    #total = 0
    #print(mst)
    #for aresta in mst:
    #    total += aresta[2]
    #print(total)

    