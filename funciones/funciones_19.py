# funcion maximo de dos números
#from operator import truediv

def inversa(x):
    a = ''
    for i in range(len(x)-1,-1,-1):
        a += x[i]
    return a 
# otra opcion    print(x[::-1])

def es_palindromo(x):
    y = inversa(x)
    if x==y:
        return True
    else:
        return False



def es_palindromo2(x):
    for i in range((len(x) // 2)+1):
        if x[i] != x[len(x) - 1 -i ]:
            print(i)
            return False
    return True



def superposicion(x,y):
    encontrado = False
    for i in x:
        if i in y:
            encontrado = True
            break
    return encontrado


