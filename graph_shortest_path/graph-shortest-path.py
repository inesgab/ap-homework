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




