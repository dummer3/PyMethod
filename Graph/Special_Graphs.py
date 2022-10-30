# This file must be renamed Special_Graphs.py

# ------ Hypercube graphs -------


def hypercube_graph(d):
    """Constructs the hypercube graph of dimension d and write it in file Hd.
    Each vertex is associated to a binary word of length d.
    For example '001101' is a vertex of hypercube of dimension 6.
    Two vertices are neighbors iff they differ on exactly one bit.
    For example, 01001 and 01101 are neighbors in hypercube(5)."""
    
    s = ['']*d
    def creation_vertice(n):
        s[n] = '0'
        if n < d-1 :
            yield from creation_vertice(n+1)
        else :
            yield s
        s[n] = '1'
        if n < d-1 :
            yield from creation_vertice(n+1)
        else :
            yield s
             
    with open(f"H{d}","w",encoding = "utf-8") as f:
        for i in creation_vertice(0):
       
            v = "".join(s)
            f.write(v + ':' + ':'.join(\
                [v[0:i] + ('0' if v[i] == '1' else '1') + v[i+1:] for i in range(d)])+ '\n')

# ------ Complete graphs -------

def complete_graph(n):
    """Constructs a complete graph of n vertices and write it in file Kn."""
    list_vertices = [f"vertice n°{x}" for x in range(1,n+1)]
    with open(f"K{n}","w",encoding = "utf-8") as f:
        for vertice in list_vertices[:-1]:
            f.write(str(vertice) + ':' + ':'.join(\
                [l for l in list_vertices if l != vertice])+ "\n")
        f.write(list_vertices[-1] + ':' + ':'.join(\
            [l for l in list_vertices if l != list_vertices[-1]])+ "\n")
            

# ------ Grid graphs -------

def grid_graph(p, q):
    """Constructs a grid pXq and write it in file GridpXq."""
    s = [0]*2
    def creation_vertice():
        for n in range(1,p+1):
            s[0] = n
            for m in range(1,q+1):
                s[1] = m
                yield s
                
    with open(f"Grid{p}X{q}","w",encoding = "utf-8") as f:
        for i in creation_vertice():
            
            f.write(''.join([str(a) for a in i]))
            if i[0] > 1 : 
                f.write(':' + ''.join([str(a) for a in [i[0]-1,i[1]]]))
            if i[0] < p : 
                f.write(':' + ''.join([str(a) for a in [i[0]+1,i[1]]]))
            if i[1] > 1 : 
                f.write(':' + ''.join([str(a) for a in [i[0],i[1]-1]]))
            if i[1] < q :
                f.write(':' + ''.join([str(a) for a in [i[0],i[1]+1]]))
            f.write("\n")


# ------ Torus graphs -------

def torus_graph(p, q):
    """Constructs a torus pXq and write it in file ToruspXq."""
    s = [0]*2
    def creation_vertice():
        for n in range(1,p+1):
            s[0] = n
            for m in range(1,q+1):
                s[1] = m
                yield s
                
    with open(f"Torus{p}X{q}","w",encoding = "utf-8") as f:
        for i in creation_vertice():
            f.write(''.join([str(a) for a in i]))
            if i[0] > 1 : 
                f.write(':' + ''.join([str(a) for a in [i[0]-1,i[1]]]))
            else : 
                f.write(':' + ''.join([str(a) for a in [p,i[1]]]))
            if i[0] < p : 
                f.write(':' + ''.join([str(a) for a in [i[0]+1,i[1]]]))
            else: 
                f.write(':' + ''.join([str(a) for a in [1,i[1]]]))
            if i[1] > 1 : 
                f.write(':' + ''.join([str(a) for a in [i[0],i[1]-1]]))
            else: 
                f.write(':' + ''.join([str(a) for a in [i[0],q]]))    
            if i[1] < q :
                 f.write(':' + ''.join([str(a) for a in [i[0],i[1]+1]]))
            else:
                f.write(':' + ''.join([str(a) for a in [i[0],1]]))
            f.write("\n")

complete_graph(8)
hypercube_graph(8)
grid_graph(3,4)
torus_graph(4,3)
