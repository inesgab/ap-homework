def parse_graph(filename):
    D = {}
    with open(filename) as f:
        for line in f:
            source, dest, weight = line.strip().split(",")
            if source not in D:
                D[source] = {}
            D[source] = {dest : int(weight)}
    return D

#print(parse_graph("graph.csv"))


def number_partices(graph):
    sommets = set()
    for i in graph:
        sommets.add(i)
        for j in graph[i]:
            sommets.add(j)
    return len(sommets)

# print(number_partices(parse_graph("graph.csv")))

def reachables(graph, s):
    pass




