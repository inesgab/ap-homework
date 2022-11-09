import random as rd
import numpy as np

def produit(L1, L2):
    M = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            M.append((L1[i], L2[j]))
    return M


def données(noms, prénoms):
    with open("data_big.txt", "w") as fichier:
        with open(noms) as f:
            with open(prénoms) as g:
                noms = f.strip().split()
                prénoms = g.strip().split()
                names = produit(noms, prénoms)
                n = len(names)
                for i in range(10000):
                    j = rd.randint(0, n-1)
                    date = f"{rd.randint(0,28)}/{rd.randint(0,12)}/{rd.randint(2000, 2004)}"
                    fichier.write(names[j][0] + " " + names[j][1] + " " + date)
                    names.pop(j)
                    n -= 1


# correction
# cf le programme de randomdate

def bonnesdonnées(noms, prénoms):
    setfirst = set()
    setlast = set()
    with open(noms) as last:
        with open(prénoms) as first:
            for line in first:
                setfirst.add(str(line.rstrip()))
            for line in last:
                setlast.add(str(line.rstrip()))
    people = set()
    while len(people) <= 10000:
        new_person = rd.sample(setfirst, 1)[0] + " " + rd.sample(setlast, 1)[0]
        if new_person not in people:
            people.add(new_person)
    with open("data_big.txt", "w") as f:
        for elt in people:
            date = f"{rd.randint(0,28)}/{rd.randint(0,12)}/{rd.randint(2000, 2004)}"
            f.write(elt + " " + date + "\n")

bonnesdonnées("last_names.txt", "first_names.txt")

# correction 2

def index(L):
    D ={}
    for person in L:
        first = person["first_name"]
        last =  person ["last_name"]
        D[(first, last)] = person
    return D

def index2(L): #compréhension de dictionnaire
    return {(person["first_name"], person["last_name"]) : person for person in L}

def nb_firstnames(L): #compréhension d'ensemble (pas de ":")
    return len({person["first_name"] for person in L})


