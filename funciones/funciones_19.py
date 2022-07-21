# funcion maximo de dos números
#from operator import truediv

def inversa(x):
    a = ''
    for i in range(len(x)-1,-1,-1):
        a += x[i]
    return a 

def es_palindromo(x,y):
    x = inversa(x)
    print(y)
    if x==y:
        return True
    else:
        return False



def es_palindromo2(x,y):
    longitud = len(x)
    if longitud == len(y):
        for i in range(longitud):
            if x[i] != y[longitud - 1 -i ]:
                print(i)
                return False
        return True
    else:
        return False
        
def superposicion(x,y):
    encontrado = False
    for i in x:
        if i in y:
            encontrado = True
            break
    return encontrado


