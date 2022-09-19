import os
import sys

script_dir = os.path.dirname( __file__ )
#print(script_dir)
mymodule_dir = os.path.join( script_dir, '..', 'funciones')
#print(mymodule_dir)
sys.path.append( mymodule_dir )
#print (sys.path)
from funciones_1_repaso import *


# EJERCICIO 1

"""
    Decribe una variable con nombre "notas" que tenga el valor -3
    muestra su valor
"""
#notas = ejercicio_1("notas")
#print(f'El valor de la variable notas es {notas}')

# EJERCICIO 2

"""
    Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida:
    El valor de "s" es "valor de s" y el valor de y es "valor de y"
"""
#s,y = ejercicio_2()
#print(f'El valor de s es {s} y el valor de y es {y}')

# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""
name = ejercicio_1("name")
print(f'El valor de la variable name es {name} ')

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""

# EJERCICIO 7

"""
    Saca el valor absoluto de -32
    Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)
"""

# EJERCICIO 8

"""
    Tratar de reemplazar los valores que faltan en este listado --> por un -1
    L = [10, None, 8, 5, None, 20]
    1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
    2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])
"""