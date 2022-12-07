def ip_v0(IP):
    L = IP.split(".")
    M = []
    for str in L:
        M.append(int(str))
    return M

def ip_v1(IP):
    L = IP.split(".")
    M = "".join(L)
    return M.encode(encoding="utf-8")
