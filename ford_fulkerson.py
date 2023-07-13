import numpy as np
import time
import heapq
from collections import defaultdict



class Graph():
    def __init__(self):
        self._n_nodes = None
        self._n_edges = None
        self._list = None
        self._distances = None

        
    def initialize_graph(self, n_nodes, n_edges):
        self._n_nodes = n_nodes
        self._n_edges = n_edges
        self._list = None
            
    def add_edge(self, u, v, capacity):
        if self._list is None:
            print("Creating adjacence list")
            self._list = defaultdict(list)
        print("Adding capacity...{}".format(capacity))
        self._list[u].append((v, capacity))
        self._list[v].append((u, 0))

    def graph_from_gr(self, file):
        with open(file) as file:
            for linha in file:
                values = linha.split(" ")
                if values[0]=='p':
                    self.initialize_graph(n_nodes=int(values[2]), n_edges=int(values[2]))
                elif values[0]=='a':
                    self.add_edge(u=int(values[1]), v=int(values[2]), capacity=int(values[3]))

    def bfs(self, source, sink, parent):
            print("Doing BFS...")
            visited = set()
            queue = [source]
            visited.add(source)
            parent[source] = -1

            while queue:
                u = queue.pop(0)

                for v, capacity in self._list[u]:
                    if v not in visited and capacity > 0:
                        queue.append(v)
                        visited.add(v)
                        parent[v] = u
                        if v == sink:
                            return True
            return False
                

    def dfs(self, u, visited, min_capacity, sink):
        visited.add(u)
        print("Doing DFS - vertice: {}".format(v))
        if u == sink:
            return min_capacity

        for v, capacity in self._list[u]:
            if v not in visited and capacity > 0:
                flow = self.dfs(v, visited, min(min_capacity, capacity), sink)
                if flow > 0:
                    for i, (x, _) in enumerate(self._list[u]):
                        if x == v:
                            self._list[u][i] = (x, capacity - flow)
                            break
                    for i, (x, _) in enumerate(self._list[v]):
                        if x == u:
                            self._list[v][i] = (x, capacity + flow)
                            break
                    return flow

        return 0
        
    def ford_fulkerson(self, source, sink):
        max_flow = 0
        parent = {}
        flows = defaultdict(int)

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            v = sink

            while v != source:
                u = parent[v]
                for i, (x, capacity) in enumerate(self._list[u]):
                    if x == v:
                        path_flow = min(path_flow, capacity)
                        break
                v = u

            v = sink
            while v != source:
                u = parent[v]
                for i, (x, capacity) in enumerate(self._list[u]):
                    if x == v:
                        flows[(u, v)] += path_flow
                        flows[(v, u)] -= path_flow
                        self._list[u][i] = (x, capacity - path_flow)
                        break
                for i, (x, capacity) in enumerate(self._list[v]):
                    if x == u:
                        self._list[v][i] = (x, capacity + path_flow)
                        break
                v = u

            max_flow += path_flow

        return max_flow, flows
                    

if __name__=="__main__":
    grafo = Graph() 
    
    grafo.initialize_graph(n_nodes=6, n_edges=8)
    grafo.graph_from_gr("/home/jaimel/Projetos/AlgoritmosGrafos/grafo_fluxo.gr")
    max_flow, flows = grafo.ford_fulkerson(source=1, sink=6)
    print("Fluxo máximo:", max_flow)
    for (u, v), flow in flows.items():
        print(f"Fluxo da aresta ({u}, {v}): {flow}")