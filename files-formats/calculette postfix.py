operators = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x//y
}

def postfix_eval(chaine):
    L = []
    for i in chaine.split():
        if i in operators:
            try: 
                b = L.pop()
                a = L.pop()
            except:
                return "error-empty-stack"
                break
            result = operators[i](a, b)
            L.append(result)
        else:
            try:
                L.append(int(i))
            except:
                return "error-syntax"
    if len(L) != 1:
        return "error-unfinished"
    else:
        return L[0]