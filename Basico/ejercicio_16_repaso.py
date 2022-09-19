import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1

# 1) Lee con pandas el archivo train.csv correspondiente al titanic dataset

df = pd.read_csv("c:/PY/datascience/train.csv")
print(df)

def print_grafico(df):
    columnas=('Pclass','Sex','Embarked')
    for i in columnas:
        pd.crosstab(df[i],df['Survived']).plot(kind="bar")
        plt.show()

#print_grafico(df)


"""
    2) Hacer un bucle for para automatizar las gráficas de pd.crosstab

    Se pide relacionar la columna Survived con Pclass, Sex y Embarked

    Nota:

    Se pide que dentro del bucle for se encuentre la gráfica requerida.

    Entonces, en una sola celda, tenemos 3 gráficas mostradas y todo automatizado.
"""

"""
    3) Hacer una función para automatizar las gráficas de pd.crosstab

    Se pide relacionar la columna Survived con Pclass, Sex y Embarked

    NOTA:

    Se pide definir una función (1 vez por ello)

    y hacer llamadas a la función (3 en este caso, para: Pclass, Sex, Embarked)
"""

def print_grafico_individual(df,columna):
    pd.crosstab(df[columna],df['Survived']).plot(kind="bar")
    plt.show()


#print_grafico_individual(df,'Pclass')
#print_grafico_individual(df,'Sex')
#print_grafico_individual(df,'Embarked')



# EJERCICIO 2

# Ejercicio de obtener los valores que muestra el pd.crosstab de Sex y Pclass sin usar el propio pd.crosstab

# 1) Imprime nuevamente los primeros 5 valores
print(df.head())


# 2) Usando value_counts() observa cuantos hombres y mujeres hay

    # (No hace falta plotear, simplemente mostrar los números de cada)
print(df["Sex"].value_counts())

# 3) Sin usar value_counts() observa cuantos hombres y mujeres hay (con un algoritmo)
def cuenta_sexo(df):
    hombre = 0
    mujer = 0
    for i in df['Sex']:
        if i == "female":
            mujer += 1
        elif i == "male":
            hombre += 1
    print(f'El valor de hombres es {hombre}')
    print(f'El valor de mujer es {mujer}')

cuenta_sexo(df)
"""
    4) Ahora haz lo mismo de otra forma

    En esta ocasión se pide que:

    crees un dataframe con el formato del original,

    bajo la permisa que sea un dataframe con todo hombres (primeramente) y con todo mujeres (a continuación)

    (2 DataFrames por tanto)

    Y observes si el número de filas de ambos nuevos DataFrames coincide con los valores anteriores
"""
def crea_dataframe_sexo(df):
   
    df_1 = df.loc[df["Sex"]=="male"]
    print(f' valores de hombre = {df_1.Sex.value_counts()}')
    df_2 = df.loc[df["Sex"]=="female"]
    print(f' valores de mujer = {df_2.Sex.value_counts()}')


crea_dataframe_sexo(df)
