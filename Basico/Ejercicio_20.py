import os
import sys

script_dir = os.path.dirname( __file__ )
#print(script_dir)
mymodule_dir = os.path.join( script_dir, '..', 'funciones')
#print(mymodule_dir)
sys.path.append( mymodule_dir )
#print (sys.path)
from funciones_20 import *

while True:
    try:
        print('\n')
        ejercicio = int(input('introduce el número del ejercicio que quieres ejecutar (0 para finalizar) '))
        if ejercicio in [1, 2, 3, 4, 5, 6, 7, 8]:
            if ejercicio == 1:
                caracter = input('introduce el caracter a duplicar  ')
                veces = int(input('introduce el número de veces que quieres duplicar el caracter'))
                result = generar_n_caracteres(veces, caracter)
                if result != None:
                    print (f'La cadena repetida es: {result} ')
                else:
                    print('Algún error se ha producido ')

            elif ejercicio == 2:
                valor1 = input('introduce la lista ')
                if valor1[0]=="[" or valor1[0]=="(":
                    valor1 = eval(valor1)
                    procedimiento(valor1)
                else:
                    print('El valor introducido no es una lista')
        
            elif ejercicio == 3:
                valor1=[]
                valor1 = input('introduce la lista de palabras ')
             
                if valor1[0]=="[" or valor1[0]=="(":
                    valor1 = eval(valor1)
                  
                    palabra,longitud = mas_larga(valor1)
               
                    print(f'la palabras que tienen mayor longitud son {palabra} y la longitud es  {longitud} ')
                else:
                    print('El valor introducido no es una lista') 
            elif ejercicio == 4:
                valor1 = []
                valor1 = input('introduce la lista a comparar   ')
                veces = int(input('introduce el número de caracteres que quieres comparar'))
                if valor1[0]=="[" or valor1[0]=="(":
                    valor1 = eval(valor1)
                    lista_aux=filtrar_palabras(valor1, veces)
                    print(f'Las palabrass con más de {veces} caracteres son {lista_aux}')
                else:
                    print('El valor introducido no es una lista') 
            elif ejercicio == 5:    
                valor1 = input('introduce la cadena a comparar   ')
                mayusculas, cad_aux = c_mayusculas(valor1)
                print(f'la mayúsculas que se tienen en la cadena son {mayusculas} y aparecen {cad_aux} ')
            elif ejercicio == 6:    
                pass
            elif ejercicio == 7:    
                nombres_buscados,cuantos = main()
            elif ejercicio == 8:
                contar_vocales()
        elif ejercicio == 0:
            break
    except Exception:
        print('error al introducir los datos')
        break        
    







"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, caracter):
    # TODO: tome un entero n
    # TODO: devuelva el caracter multiplicado por n
    pass

# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""

def procedimiento(lista):
    # TODO: tome una lista de numeros enteros
    # TODO: imprimir en la pantalla:

    # XXXX
    # XXXXXXXXX
    # XXXXXXX
    pass

# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(lista):
    # TODO: tome una lista de palabras
    # TODO: devolver la más larga
    pass

# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista, n):
    # TODO: tome una lista de palabras y un entero n
    # TODO: devolver las palabras que tengan n caracteres
    pass

# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def c_mayusculas(cadena):
    # TODO: ingrese una cadena de texto
    # TODO:evaluar la cadena
    # TODO: returnar cuantas letras mayúsculas tiene
    pass

# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""

def mayores(tup):
    # TODO: definir una tupla de 10 edades de personas
    # TODO: imprimir la cantidad de personas con edades superiores a 20
    pass

# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def main():
    # TODO: definir cuantos nombres quieres ingresar
    # TODO: definir una lista con el numero de elementos
    # TODO: pedir los nombres que pertenecen a la lista
    # TODO: definir por que letra comienza el nombre
    # TODO: imprimir la cantidad de nombres que empiezan por la letra
    pass

# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

def contar_vocales(cadena):
    # TODO: recibir una palabra
    # TODO: contabilizar cuantas letras tiene de "a"
    # TODO: contabilizar cuantas letras tiene de "e"
    # TODO: contabilizar cuantas letras tiene de "i"
    # TODO: contabilizar cuantas letras tiene de "o"
    # TODO: contabilizar cuantas letras tiene de "u"
    pass
