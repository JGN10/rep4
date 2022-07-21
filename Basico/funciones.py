# funcion maximo de dos números
#from operator import truediv


def maximo(x,y):
    
    if x > y:
        return (x)
    elif x < y:
        return (y)
    else:
        return (None)



def max_de_tres(x,y,z):
    max1 = maximo(x,y)
    if max1 != None:
        return (maximo(max1,z))
    else:
        return None




def longitud(x):
    try:
        i=0
        while True:
            var = x[i]
            i += 1
    except IndexError:
        return(i)



def es_vocal(x):
    vocales = ['A','E','I','O','U']
    if x.upper()  in vocales:
        return True
    else:
        return False


def suma_lista(x):
    suma = 0
    try:
        for i in range(longitud(x)):
            suma += x[i]
        return suma
    except TypeError:
        return None



def mult_lista(x):
    mult = 1
    var1 = 0
    try:
        for i in range(longitud(x)):
            
            mult = (mult * int(x[i]))
        return mult
    except Exception:
        return None
#print(mult_lista([1,2,3,4]))
