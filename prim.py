import numpy as np
import time
import heapq



class Graph():
    def __init__(self, dir):
        self._n_nodes = None
        self._n_edges = None
        self._list = None
        self._distances = None
        self._dir = dir
        
    def initialize_graph(self, n_nodes, n_edges):
        self._n_nodes = n_nodes
        self._n_edges = n_edges
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
                    self.initialize_graph(n_nodes=int(values[2]), n_edges=int(values[2]))
                elif values[0]=='a':
                    self.add_edge(u=int(values[1]), v=int(values[2]), weight=int(values[3]))

    def prim(self, root):
        start_time = time.time()
        H = []
        for (v, c) in self._list[root]:
            heapq.heappush(H, (c, root, v))
        
        n_tree_edges = 0
        total_coust = 0
        closed_vert = [root]
        mst = []

        #laço principal do algoritmo
        while n_tree_edges < self._n_nodes-1:
            print("Adding {} edge in tree of {} total edges".format(n_tree_edges+1, self._n_nodes-1))
            #esse laço é porque as arestas que não serão utilizadas não estão sendo retiradas da heap, porque isso ficaria custoso. Mas como
            #os extremos das arestas já estão na árvore esse loop garante que os nós não sejam incluídos.
            while True:
                #quando eu insiro na heap, o vértice "u" nó já está marcado, então, basta eu verificar se o vértice "v" está marcado.
                (c, u, v) = heapq.heappop(H)
                if v not in closed_vert:
                    break
            closed_vert.append(v)
            total_coust += c
            mst.append((u,v))
            n_tree_edges += 1
            #aumento o meu conjunto de arestas candidatas, colocando as arestas vizinhas dos vizinhos de "v"
            for (neib, c) in self._list[v]:
                if neib not in closed_vert:
                    heapq.heappush(H, (c, v, neib))

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Prim time: {elapsed_time:.8f} seconds")
        return mst, total_coust

    def show_distances(self):
        print(self._distances)
                    

if __name__=="__main__":
    grafo = Graph(dir=True)
    
    #Exemplo toy1
    '''
    grafo.initialize_graph(10, 19)
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
    #grafo.dijkstra(1)
    #grafo.show_distances()
    mst, total_coust = grafo.prim(1)
    print("Custo total Prim: {}".format(total_coust))

    
