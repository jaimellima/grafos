import numpy as np

def malgrange(G, V, C, i):
    v = V.pop()
    R = {v}
    Y = set()
    while len(N(R,G) - R) !=0:
        Y = (N(R,G) - R)
        R = R.union(Y)
    Y = R
    V = V - Y
    C[i] = R
    if len(V)!=0:
        i+=1
        v = V.pop()
        malgrange(G, V, C, i)
    else:
        print(C)
    
def N(R,G):
    N = set()
    for v in R:
        for i, valor in enumerate(G[v]):
            if valor==1:
                N.add(i)
    return N

def malgrange_adap(G):
    Y = set([i for i, valor in enumerate(G[0])])
    i = 0
    componentes = {}
    while len(Y)!=0:
        R = set() #armazena os vizinhos do vértice
        R_ = set()
        v = Y.pop() #escolhe um vértice
        W = set()
        R = {v}
        while W!=(R.union(N(R, G))):
            R = R.union(N(R, G))
            W = R
        W = set()
        R_ = {v}
        while W!=(R_.union(N_(R_, G))):
            R_ = R_.union(N_(R_, G))
            W = R_
        componentes[i] = R_.intersection(R)
        Y = Y - componentes[i]
        i+=1
    print(componentes)

def N(R, G):
    N = set()
    for v in R:
        for i, valor in enumerate(G[v]):
            if valor!=0:
                N.add(i)
    return N

def N_(R_, G):
    N = set()
    for v in R_:
        for i, valor in enumerate(G[:,v]):
            if valor!=0:
                N.add(i)
    return N

if __name__=="__main__":
    
    G = [
        [0, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0]
        ]
    
    G1 = [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 0],
        ]
    G2 = [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        ]
    
    G3 = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1],
        ]
    G4 = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        ]
    G = np.array(G2)
    malgrange_adap(G)
    V = set([i for i, valor in enumerate(G[0])])
    C = {}
    i = 0

    #malgrange(G, V, C, i)
    





    

