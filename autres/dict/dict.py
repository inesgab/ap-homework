
def dict(filename):
    D =[]
    with open(filename) as f:
        for line in f:
            d = {}
            L = line.strip().split(" ")
            d["prénom"] = L[0]
            d["nom"] = L[1]
            d["date de naissance"] = (L[2], L[3], L[4])
            D.append(d)
    return D

print(dict("données.txt"))

#correction
def dict2(filename):
    D =[]
    with open(filename) as f:
        for line in f:
            d = {}
            first, last, *birth = line.strip().split()
            d["prénom"] = first
            d["nom"] = last
            d["date de naissance"] = birth
            D.append(d)
    return D