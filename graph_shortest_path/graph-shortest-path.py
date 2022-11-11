G = {'a': {'b': 7, 'd': 9, 'c': 14},
     'b': {'d': 10, 'e': 15},
     'c': {'d': 2, 'f': 9},
     'd': {'e': 11},
     'e': {'f': 6}}
#exo 1
def parse_graph(filename):
    D = {}
    with open(filename) as f:
        for line in f:
            source, dest, weight = line.strip().split(",")
            if source not in D:
                D[source] = {}
            D[source][dest] = int(weight)
    return D

#print(parse_graph("graph.csv"))

#exo 2
def number_partices(graph):
    sommets = set()
    for i in graph:
        sommets.add(i)
        for j in graph[i]:
            sommets.add(j)
    return len(sommets)

# print(number_partices(parse_graph("graph.csv")))

# exo 3 (je ne vois pas comment faire à partir de seulement graph et s)
def reachables(graph, s, reached):
    if s not in reached:
        reached.add(s)
        if s in graph:
            for i in graph[s]:
                reached | reachables(graph, i, reached)
    return reached
        
# print(reachables(parse_graph("graph.csv"), 'd', set()))

# exo 4
import math

def shortest_distance(graph, v1, v2):

    # initialisation
    # on se définit une variable locale à la fonction
    # qui matérialise le marquage

    visited = {}
    visited[v1] = 0
    # ensuite on fait une boucle jusqu'à ce que la condition soit remplie
    while True:

        # les arêtes qui satisfont le critère 
        edges = {}

        # on énumère toutes les arêtes, et on ajoute dans
        # edges celles qui satisfont le critère
        for i in visited:
            if i in graph:
                for j in graph[i]:
                    if j not in visited:
                        edges[j] = visited[i] + graph[i][j]


        # si on n'a aucune arête c'est que c'est raté
        if not edges:
            return None

        # sinon on trouve la meilleure
        shortest_length = math.inf
        shortest_vertex = None
        for j in edges:
            if edges[j] < shortest_length:
                shortest_length = edges[j] # trouver la plus courte
                shortest_vertex = j # et mémoriser le sommet correspondant

        visited[shortest_vertex] = shortest_length # marquer le sommet correspondant

        # regarder si c'est le sommet 
        if shortest_vertex == v2:
            return shortest_length

# print(shortest_distance(G, 'a', 'f'))

def path(parents, vinit, vfinal):
    v = vfinal
    path = [v]
    while v != vinit:
        v = parents[v]
        path.append(v)
    return list(reversed(path))

def shortest_path(graph, v1, v2):
    visited = {}
    visited[v1] = 0
    parents = {}
    while True:

        # les arêtes qui satisfont le critère 
        edges = {}

        # on énumère toutes les arêtes, et on ajoute dans
        # edges celles qui satisfont le critère
        for i in visited:
            if i in graph:
                for j in graph[i]:
                    if j not in visited:
                        edges[j] = (i, visited[i] + graph[i][j])


        # si on n'a aucune arête c'est que c'est raté
        if not edges:
            return None

        # sinon on trouve la meilleure
        shortest_length = math.inf
        shortest_vertex = None
        for j in edges:
            if edges[j][1] < shortest_length:
                shortest_length = edges[j][1] # trouver la plus courte
                shortest_vertex = j # et mémoriser le sommet correspondant

        visited[shortest_vertex] = shortest_length # marquer le sommet correspondant
        parents[shortest_vertex] = edges[shortest_vertex][0]
        # regarder si c'est le sommet 
        if shortest_vertex == v2:
            return shortest_length, path(parents, v1, v2)

print(shortest_path(G, 'a', 'e'))

#exo 6

