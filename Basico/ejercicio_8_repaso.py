import pandas as pd
import time 
import numpy as np

# EJERCICIO 1 

# Calcula la longitud de una cadena de texto sin usar la instruccion len(cadena)

# 1) Cadena de texto: hola como estas?

    # Nombre de la variable: "cadena"

# 2) Longitud de la cadena de texto
cadena = "hola como estas?"
longitud = 0
for i in cadena:
     longitud += 1

print(longitud)



# 3) Longitud de la cadena de texto calculada con un bucle
print(len(cadena))

# EJERCICIO 2

# Crea un diccionario que tenga la nota de 3 asignaturas y

# haz un pequeño algoritmo que calcule la nota media

# CURSO         -> Nota
# ---------------------
# Python        ->  10
# Big Data      ->  8
# NLP           ->  6

asignaturas = {"Python": 10, "Big Data": 8, "NLP":6}
# 1) Muestra el valor de las claves
print(asignaturas.keys())

# 2) Muestra el valor de los valores del diccionario
print(asignaturas.values())
# 3) Apendiza en el diccionario un nuevo elemento:
asignaturas["machine Learning"] = 9
    # Machine Learning --> 9

# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.
lista=[]
var=[]
for clave,valor in asignaturas.items():
    var.append(clave)
    var.append(valor)
    lista.append(var)
    var = []
print(lista)

    # [["clave1", valor1], ["clave2", valor2]]

# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta
asig = []
nota = []
for clave,valor in asignaturas.items():
    asig.append(clave)
    nota.append(valor)

df = pd.DataFrame(asig, columns=["Asignatura"])
df["notas"] = nota
print(df)
print(df["notas"].max())
# tambien es max(df.notas)


    

# 6) ¿y la nota más baja?
print(df["notas"].min())
# tambien es min(df.notas)
# 7) Ordena el dataframe en orden descendente:
df1 = df.sort_values(by="notas", ascending=False)
print(df1)

# EJERCICIO 3

"""
Dadas 2 funciones:

Determina cual de ellas ejecuta mas rápido.

Si sabes, hazlo de 2 formas.

función a

def main(): for i in range(10**8): pass

main()

función b

def main(): for i in np.arange(10**8): pass

main()

de 2 formas
"""

def main():
    for i in range(10**8):
        pass


def main2():
    for i in np.arange(10**8):
        pass

def mide_tiempos():
    inicio1 =time.time()
    main()
    fin1 = time.time()
    inicio2 =time.time()
    main2()
    fin2 = time.time()
    print (f'tiempo 1 {fin1-inicio1}')
    print (f'tiempo 2 {fin2-inicio2}')

#mide_tiempos()

# la otra forma sería con %%time

# EJERCICIO 4

# Dada:

# Una matriz tal que así:

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# se pide:

# 1) Escribe ese código en Python
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
def escribe_matriz(matriz):
    print(matriz)
#escribe_matriz(a)

# 2) Escribe la matriz transpuesta.
def imprime_transpuesta(matriz):
    m = matriz.transpose()
    # otra forma print(matriz.T)
    print(m)

#imprime_transpuesta(a)


    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# 3) Se pide que hagas lo mismo, pero con un bucle.
b = np.copy(a)
filas = len(b)
columnas = int(b.size/filas)
print(columnas)
for i in range(filas):
    for j in range(columnas):
       
        b[j,i]=a[i,j]
print(b)
