# EJERCICIO 1

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
    Escribir una tercera función que reciba un diccionario con los precios
    y porcentajes de una cesta de la compra, y una de las funciones anteriores, 
    y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
    Ejemplo de diccionario: {1000:20, 500:10, 100:1}
"""

def apply_discount(price, discount):
    return price - ((price*discount)/100)
   


def apply_IVA(price, percentage):
    return price + ((price*percentage)/100)


 
def price_basket(basket, func):
    for importe,porcentaje in basket.items():
        print(f'El resultado de aplicar la función con los valores del importe {importe} y el {porcentaje}% es {func(importe,porcentaje)}')

dic_descuento = {1000:10, 2000:20, 3000:30}
dic_iva = {1000:15, 2000:25, 3000:35}
#price_basket (dic_descuento,apply_discount)
#price_basket (dic_iva,apply_IVA)

# EJERCICIO 2

"""
    Escribir una función que reciba otra función y una lista,
    y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista.
"""
def longitud(x):
    return (len(x))


def aplica_funcion_lista(funcion, lista):
    lista_aux = []
    for i in lista:
        lista_aux.append(funcion(i))
    return lista_aux

lista_inicial =['1','22','333','4444']
#print(aplica_funcion_lista(longitud,lista_inicial))


def cuadrado(n):
    return n*n

lista_dos =[1,2,3,4]
#print(aplica_funcion_lista(cuadrado,lista_dos))
    

# EJERCICIO 3

"""
    Escribir una función que reciba una frase y
    devuelva un diccionario con las palabras que contiene y su longitud.
    Ejemplo: "Hola Mundo" --> {"Hola": 4, "Mundo": 5}
"""
def divide_cadena(cadena):
    lista = cadena.split()
    lista_aux = []
    dic_aux = {}
    for i in lista:
        dic_aux[i] = len(i)
        lista_aux.append(len(i))
    print(lista_aux)    
    return dic_aux
    
    

#print (divide_cadena('llat lla dadfd lldald ladlfdf'))

def dev_calificaciones (x):
    if x < 5:
        return 'Suspenso'
    elif x == 5:
        return 'Aprobado'
    elif (x > 5) and (x < 7):
        return 'Suficiente'
    elif (x >= 7) and (x < 9):
        return 'notable'
    elif (x >= 9) and (x <= 10):
        return 'Sobresaliente'    
    else:
        return None    
        

def calificaciones(lista):
    print(lista)
    lista_aux = []
    for i in lista:
        lista_aux.append(dev_calificaciones(i))
    return lista_aux

#print(calificaciones([1,2,3,4,5,6,7,8,9,10]))

def dict_calificaciones(dict):
    print(dict)
    dict_aux ={}
    for asignatura,nota in dict.items():
        dict_aux[asignatura.upper()]= dev_calificaciones(nota)
    return dict_aux

dict_notas = {'física': 1, 'Matemáticas': 2, 'lengua': 7, 'QUÍMICA' : 10}
#print (dict_calificaciones(dict_notas))


def valida_pass(pass_almacenado):
    pass_introducido = str(input('introduce el password a comparar '))
    if pass_introducido.upper() == pass_almacenado.upper():
        return True
    else:
        return False



def pide_pass():
    clave = str(input('introduce el valor de la password a almacenar '))
    if valida_pass(clave):
        print('Se ha confirmado que el password almacenado y el introducido es el mismo')
    else:
        print('El password almacenado y el introducido NO son el mismo')

pide_pass()