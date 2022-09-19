"""
    Creado: Jerónimo Gutiérrez
    Fecha: 08/09/2022
"""

# Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt


# EJERCICIO 1

"""
    Escribe el código necesario en Python para:

    almacenar con una lista de nombre "clientes" los siguientes nombres:

    "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas",
    "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"
"""

# 1) Para ese listado de clientes imprime todos ellos, 1 a 1
def ejercicio_1_1():
    lista = ["Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas",
    "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"]
    print(lista)
    print('imprimiendo uno a uno')
    for i in lista:
        print(i)
    return lista

clientes = ejercicio_1_1()


"""
    2) Dentro de ese grupo de clientes..

    se pide buscar..al cliente de nombre: "Juan García" si es posible

    Si lo encuentra, debería imprimir un mensaje tal que así:

    "el cliente -nombre del cliente- se encuentra en mi Base de Datos de Clientes"

    Si no se le encuentra, debería salir un mensaje tal que así:

    "el cliente -nombre del cliente- NO se encuentra en mi Base de Datos de Clientes"

    Nota: Comprueba en el caso de llevar o no acento

    Para:

    Juan García

    Juan Garcia

    Ojo con la tilde..
"""
def ejercicio_1_2(lista):
    nombre = input('introduce el nombre a buscar: ')
    # una form
    # a = (map(lambda x: x.lower(), clientes)) 
    # clientes = list(a)
    #lo cambia a lower, pero lo está recorriendo 

    #otra forma 
    # pd_d = list(pd.serires(clientes).str.lower()) 
    # print(pd_d)
    if nombre in lista:
        print(f"el cliente {nombre} se encuentra en mi Base de Datos de Clientes")
    else:
        print(f"el cliente {nombre} NO se encuentra en mi Base de Datos de Clientes")

#ejercicio_1_2(clientes)

def ejercicio_1_2_upper(lista):
    try:
        nombre = input('introduce el nombre a buscar: ')
        encontrado = 0
        for i in lista:
            if i.upper() == nombre.upper():
                print(f"el cliente {nombre} se encuentra en mi Base de Datos de Clientes")
                encontrado = 1
                break
        if encontrado == 0:
            print(f"el cliente {nombre} NO se encuentra en mi Base de Datos de Clientes")
    except Exception as e:
        print("error en bucle for %s" % str(e))


#ejercicio_1_2_upper(clientes)

"""
    3) Crea un DataFrame, de nombre df

    con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)

    clientes: Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas,
            Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González

    tarifas: 40,50,50,35,45,50,60,50,45
"""
def crea_df(lista):
    tarifas = [40,50,50,35,45,50,60,50,45]
    df_aux = pd.DataFrame()
    df_aux["clientes"] = lista
    df_aux["tarifas"] = tarifas
    return df_aux

df = crea_df(clientes)

# 4) Imprime las primeras 5 filas del DataFrame de 2 formas distintas
def imprime_lineas(df_aux):
    lineas = int(input('introduce las líneas a imprimir '))
    print(df.head(lineas))

#imprime_lineas(df)


# 5) De ese DataFrame, selecciona solamente la columna "tarifas" e imprímela
    # (con 1 forma es suficiente, pero si sabes 2 mejor)
def selecciona_columna(df_aux):
    columna = str(input('introduce la columna a mostrar: '))
    print(df_aux[columna])
    print(df.loc[:,columna])
    print(df.columna)

#selecciona_columna(df)


# 6) Descomenta las siguientes líneas (algunos trucos y cosas útiles).
    # Ponlo en formato función!!
def funcion(df):
    #df.tarifas.value_counts()
    #df.tarifas.value_counts().plot(kind="bar")
    #plt.show()
    df.tarifas.plot(kind="bar")
    plt.show()
    print(df)

#funcion(df)

# 7) De ese DataFrame, selecciona solamente aquellos clientes con tarifa superior a 50 euros (50 no incluído)
def filtra_tarifa(df_aux):
    valor = int(input('introduce el valor por el que filtrar '))
    print(df_aux[(df_aux['tarifas'] > valor)])

#filtra_tarifa(df)

# EJERCICIO 2

# Número par o impar

# Prueba para los números 6 y 3

# Realiza un algortimo para saber si son pares o impares
def es_par():
    numero = int(input('introduce el valor del número a comparar '))
    if numero%2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} no es par')

#es_par()

# EJERCICIO 3

"""
    Intercambio de valores entre variables

    Siendo por ejemplo:

    x = 3 e y = 2
    Se pide hacer un pequeño algoritmo que me intercambie esos valores.

    Y que sea el resultado:

    x = 2 e y = 3
"""

# 1) Hazlo sin funciones
x = 3
y = 2
print (f'El valor de x es {x} y el valor de y es {y}')
x,y=y,x
print (f'El valor de x es {x} y el valor de y es {y}')

# 2) Hazlo mismo con una función
def intercambia_valor(x,y):
    return y,x
x = 3
y = 2
print (f'El valor de x es {x} y el valor de y es {y}')
x,y = intercambia_valor(x,y)
print (f'El valor de x es {x} y el valor de y es {y}')
