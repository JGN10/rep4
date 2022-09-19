
# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""

def ordenar_numero(valor1, valor2):
    if valor1 <= valor2:
        return valor2,valor1
    elif valor2 <= valor1:
        return valor1,valor2
    else:
        return valor1,valor2

mayor, menor = ordenar_numero(123,97)        
print(f'el valor mayor {mayor}')
print(f'el valor menor {menor}')


# EJERCICIO 2

"""
    Definir una función max_de_tres(),
    que tome tres números como argumentos y
    devuelva el mayor de ellos.
"""
def mayor_de_tres(valor1,valor2,valor3):
    mayor,menor=ordenar_numero(valor1,valor2)
    mayor,menor=ordenar_numero(mayor,valor3)
    return mayor, menor

mayor1,menor1 = mayor_de_tres(234,999,32)
print(f'El valor mayor es {mayor1}')


# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista
    o una cadena dada.
    (Es cierto que python tiene la función len() incorporada,
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
def longitud_cadena(valor):
    longitud = 0
    for i in valor:
        longitud += 1
    return longitud

print(f'la longitud de la cadena {longitud_cadena("la longitud de la cadena")}')

# EJERCICIO 4


"""
    Escribir una función que tome un carácter y devuelva True si es una vocal,
    de lo contrario devuelve False.
"""
def es_vocal(valor):
    vocales = 'AEIOU'
    if valor.upper() in vocales:
        return (f'{valor} es vocal')
    else:
        return (f'{valor} no es vocal')

print(es_vocal('r'))
print(es_vocal('e'))



# EJERCICIO 5

"""
    Escribir una función suma() y una función multip() que sumen y multipliquen
    respectivamente todos los números de una lista.
    Por ejemplo: suma([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""


def suma(valor):
    suma = 0
    for i in valor:
        suma += i
    return suma

   
def multip(valor):
    multip = 1
    for i in valor:
        multip *= i
    return multip

print(f"el valor da la suma: {suma([5,6,7])} ")
print(f"el valor da la multiplicación: {multip([5,6,7])} ")
