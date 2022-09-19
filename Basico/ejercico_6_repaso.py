import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1
listado=[30, 20, 10, 50, 40]
# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40
def ejercicio1(lista):
    minimo=lista[0]
    print(lista)
    print(type(lista))
    print(f"El mínimo de la lista es {min(lista)}")
    for i in lista:
        if minimo > i:
            minimo = i
    print(f"El mínimo de la lista (por bucles) es {minimo}")
    

#ejercicio1(listado)

# 1) Escribe el listado e ímprimelo

# 2) Prueba con min(listado)

# 3) Realiza lo mismo pero con bucles y condicionales


# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

# 2) Prueba con max(listado)

# 3) Realiza lo mismo pero con bucles y condicionales

def ejercicio2(lista):
    maximo=lista[0]
    print(lista)
    print(type(lista))
    print(f"El máximo de la lista es {max(lista)}")
    for i in lista:
        if maximo < i:
            maximo = i
    print(f"El máximo de la lista (por bucles) es {maximo}")

#ejercicio2(listado)


# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales
def ejercicio3(lista):
    print(f'listado antes del sort {lista}')
    listado_ascendente = lista.sort()
    print(f'listado ascendente con sort  {lista}')

def ejercicio3_bucle(lista):
    print(f'listado antes del bucle {lista}')
    listado_ascendente = []
    for i in range(0,len(lista)):
        minimo = lista[0]
        for j in lista:
            if minimo > j:
                minimo = j
        lista.remove(minimo)
        listado_ascendente.append(minimo)

    print(f'listado ascendente con bucle {listado_ascendente}')

listado2 = listado.copy()
#ejercicio3(listado)    
#ejercicio3_bucle(listado2)



# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales
def ejercicio4(lista):
    print(f'listado antes del sort {lista}')
    listado_descendente = lista.sort(reverse=True)
    print(f'listado descendente con sort {lista}')

def ejercicio4_bucle(lista):
    
    print(f'listado antes del bucle {lista}')
    listado_descendente = []
    for i in range(0,len(lista)):
        maximo = lista[0]
        for j in lista:
            if maximo < j:
                maximo = j
        lista.remove(maximo)
        listado_descendente.append(maximo)

    print(f'listado descendente con bucle {listado_descendente}')

#listado=[30, 20, 10, 50, 40]
#listado2 = listado.copy()
#ejercicio4(listado)    
#ejercicio4_bucle(listado2)



# EJERCICIO 5
"""
    Escribe el código necesario en Python para:
    * almacenar con una lista de nombre "módulos" las siguientes materias de un programa de Ciencia de Datos:
    * Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.
"""
# 1) Para ese listado imprime todas ellas, 1 a 1
def ejercicio5_1():
    listado =['Big Data', 'Python', 'Algoritmos', 'Machine Learning', 'Deep Learning', 'NLP']
    print('los valores de la lista son ')
    for i in listado:
        print(i)
    return listado

modulos = ejercicio5_1()
#print(modulos)

"""
    2) dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.
    y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.
    Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)
    Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)
    Imprime ese listado al terminar de almacenarlos.
"""
def ejercicio5_2(listado):
    lista =[]
    for i in listado:
        if (i == 'Python') or (i == 'Algoritmos'):
            lista.append(i)
    print('los valores esenciales')        
    for j in lista:
        print(j)
    return lista

esenciales = ejercicio5_2(modulos)
#print(esenciales)

"""
    3) Crea un DataFrame, de nombre df con esa información en base
    a la siguiente relación de módulos y horas de clase módulos:
    Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP
    horas: 25, 15, 5, 15, 5, 10
"""


def ejercicio5_3(listado):
   
    horas = [25, 15, 5, 15, 5, 10]
    #df1 = añade_columna_df(df1,modulos,"Modulos")
    df1=pd.DataFrame({"Módulos" : modulos})
    print(df1)
    #df1 = añade_columna_df(df1,horas,"Horas")
    df1["horas"] = horas
    print(df1)
    return df1

print('ejercicio 5_3')
df = ejercicio5_3(modulos)
print(df)


# 4) De ese DataFrame, selecciona solamente la columna "horas" e imprímela
def selecciona_columna(df1,columna):
    print(f'imprimiendo la columna {columna}' )
    print(df1[columna])
    # también valdria print(df1.horas) y print(df[["horas"]])
print('ejercicio 5_4')
selecciona_columna(df,"horas")

# 5) Muestra el gráfico (plot) para la columna "horas"
def grafico_df(df1,columna):
    datos = df1[columna]
    figure = datos.plot(kind="bar")
    plt.show()


grafico_df(df,"horas")


# 6) De ese DataFrame, selecciona solamente aquellas materias que tienen 20 o más horas de dedicación
def selecciona_mayor(df1,horas):
    print(df1[(df1["horas"] > horas)])

#selecciona_mayor(df,20)

# 7) De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación
def selecciona_menor(df1,horas):
    print(df1[(df1["horas"] < horas)])

#selecciona_menor(df,10)

# 8) De ese DataFrame, selecciona solamente (si fuera posible)
    # aquellas materias que tienen mas de 26 horas de dedicación
def selecciona_igual(df1,horas):
    print(df1[(df1["horas"] == horas)])

#selecciona_igual(df,26)

# 9) Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.

    # Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia
def añade_columna_df(dataf,lista,nombre):
    dataf[nombre] = lista
    return dataf

def ejercicio5_9(df1):
    docente =['Enrique', 'Susana', 'Juan', 'Ana', 'Laura', 'Patricia']
    df1 = añade_columna_df(df1,docente,"docente")
    print(df1)

#ejercicio5_9(df)

