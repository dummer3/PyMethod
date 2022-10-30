import random
import Special_Graphs

"""A vertex is a string.
A graph is a dictionary; its keys are vertices and the value associated to a
key/vertex u is the set of neighbors of u in G.
"""

def extract_graph_from_file(file):
    """Takes a file name as input and extracts the graph inside it.
    The file is composed of n lines, where n is the total number of vertices.
    Each line is of the form u:v1:v2:...:vk where u is a vertex and the
    vi's are its neighbors. If u has no neighbor, the corresponding line is u:
    This function returns a dictionary representing the graph:
    Its keys are vertices and its values are the sets of neighbors
    of each vertex. """
    with open(file,"r",encoding="utf-8") as f:
        dic = {}
        for l in f:
            s = l.strip().split(":")
            dic[s[0]] = set(s[1:])
        return dic


def set_of_vertices(graph):
    """Returns the set of vertices of the graph."""
    return set(graph.keys())


def set_of_neighbors(graph, u):
    """Returns the set of neighbors of vertex u in the graph."""
    return graph[u]


def degree_of(graph, u):
    """Returns the numbers of neighbors of vertex u in the graph."""
    return len(graph[u])


def are_neighbors(graph, u, v):
    """Boolean function returning True if u and v are neighbors in the graph.
     Returns False otherwise."""
    return v in graph[u]


def number_of_vertices(graph):
    """Returns the number of vertices of the graph."""
    return len(set_of_vertices(graph))


def number_of_edges(graph):
    """Returns the number of edges of the graph.
    We suppose that it is NON directed."""
    
    return sum([degree_of(graph, v) for v in graph])//2
          

def is_symmetric(graph):
    """Boolean function returning True if the dictionary representing the graph
    is symmetric: u is a neighbor of v iff v is a neighbor of u.
    Returns False otherwise and print a non symmetric couple."""

    for vertex in graph.keys():
        for edge in graph[vertex]:
            if not are_neighbors(graph,edge,vertex):
                print(f"{edge} and {vertex} are not symetric")
                return False
    return True

def bfs(graph, r):
    """Makes the BFS of the graph from vertex r. Returns a tuple
    (parent, d, color)."""
    
    couleur = {s:'blanc' for s in set_of_vertices(graph)}
    d =       {s:None     for s in set_of_vertices(graph)}
    parent =  {s:None    for s in set_of_vertices(graph)}

    F = [r]
    couleur[r]='gris'
    d[r]      =0
    
    while F != []:
        u = F[0]

        print(u)
        for v in graph[u]:
            if couleur[v] == 'blanc':
                F.append(v)
                couleur[v]='gris'
                d[v]      = d[u]+1
                parent[v] = u
        F = F[1:]
        couleur[u]= 'noir'

    return (parent,d,couleur)


def color_graph_by_list(graph, list_of_vertices):
    """Takes as input a graph and a list of its vertices. This function colors
    the graph with this list and returns a tuple (c, color) where:
     + color is the constructed coloration (a dictionary whose keys are the
     vertices and values are colors (integers > 0)) and
     + c is the number of colors used by the coloration color."""
    color = {list_of_vertices[0]:1}
    color_max = 1
    for vertice in list_of_vertices[1:]:
        good_color = True
        for i in range(1,color_max+1):
            good_color = True
            for edge in graph[vertice]:
                if edge in color.keys():
                    if i == color[edge]:
                        good_color = False
                        
            if good_color == True:
                  color[vertice] = i
                  break
        if good_color == False:
            color_max += 1
            color[vertice] = color_max
    return (color_max,color)

def color_graph_by_random_lists(graph, number_of_iterations=1):
    """Takes as input a graph, and an integer number_of_iterations.
    Runs number_of_iterations times the coloring function of the graph on
    random lists of vertices of the graph and returns the best coloring found
    (the one using the lowest number of colors)."""
    list_of_vertices = list(graph.keys())
    (color_min,dico_min) =  color_graph_by_list(graph,list_of_vertices)
    for _ in range(number_of_iterations-1) :
        random.shuffle(list_of_vertices)
        c,dic = color_graph_by_list(graph,list_of_vertices)
        if c < color_min:
            dico_min = dic
    return dic
        


def is_stable(graph, set_s):
    """Boolean function taking as input a graph and a set of vertices.
    It returns True if this set is a stable of the graph (there is no edge
     between vertices of this set in the graph).
     Returns False otherwise."""
    for vertice in set_s:
        for edge in graph[set_s]:
            if edge in set_s :
                return False
    return True

def is_proper_coloring(graph, color):
    """Takes as input a graph and a coloring (a dictionary having the set of
    vertices as keys and colors (integers > 0) as values).
    Returns True if color is a proper coloring of the graph.
    Returns False otherwise and print a message to indicate the error."""
    dico_range_par_val = {}
    for key, val in color.items():
        if val in dico_range_par_val.keys():
            dico_range_par_val[val].append(key)
        else :
            dico_range_par_val[val] = []
    for val in dico_range_par_val:
        if is_stable(graph,key) == False:
            return False
    return True



l = [2,3,4]
l.append(1);
print(l)
