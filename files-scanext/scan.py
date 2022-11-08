from pathlib import Path
from datetime import datetime as DateTime

def scanv1(dossier, truc):
    globbing = Path(dossier)
    for p in list(globbing.glob("*.truc")):
        date = DateTime.fromtimestamp(p.stat().st_mtime)
        print(str(p.resolve()))
        print(f"{p.stat().st_size} B last modified on {date}")

# je ne vois pas comment print la première ligne avec Path

def scanv3(dossier, truc):
    L = list(truc)
    for ext in L:
        globbing = Path(dossier)
        for p in list(globbing.glob("*.ext")) :
            date = DateTime.fromtimestamp(p.stat().st_mtime)
            print(str(p.resolve()))
            print(f"{p.stat().st_size} B last modified on {date}")

#je ne vois pas comment prendre en compte
#le fait que truc soit éventuellement vide