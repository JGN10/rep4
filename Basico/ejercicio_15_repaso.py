import pandas as pd

# EJERCICIO 1


# 1) Crea una lista de nombre "Concursante" que contenga los siguientes valores:
    # "Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"

# 2) Crea una lista de nombre "Resultados" que contenga los siguientes valores:
    # 20, 30, 50, 20, 10, 5, 60, 40

# 3) Crea un diccionario con los concursantes y los resultados.

# 4) Crea un dataframe vacio y apendiza los concursantes y los resultados mediante el empleo de un bucle for

# 5) Con ayuda de loc filtra los resultados obtenidos desde Pedro hasta Lara.

# 6) Con ayuda de loc filtra los resultados obtenidos mayores o iguales a 40

# 7) Muestra el concursante con la mayor puntuación

# 8) Muestra el concursante con la menor puntuación

# 9) Modifica con la ayuda de loc los valores 20 por 0

# 10) Modifica Concursante "Juan" su puntuación por "None" con ayuda de .loc

def ejercicio_1():
    Concursante = ["Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"]
    Resultados = [20, 30, 50, 20, 10, 5, 60, 40]
    dic1 = {"Concursantes": Concursante, "Resultados":Resultados }
    print(dic1)
    """
    df = pd.DataFrame(columns=['Concursante', 'resultados'])
    for valor in range(len(Concursante)):
        dic2={"Concursante":Concursante[valor], "Resultados":Resultados[valor]}
        df.append(dic2,ignore_index=True)
    """
    df= pd.DataFrame(dic1)
    print(df)
    print(df.loc[1:5,:])
    print(df.loc[df["Resultados"]>=40])
    print(df.max())
    print(df["Resultados"].max())
    print(df.loc[df["Resultados"]==60])
    print(df.min())
    print(df["Resultados"].min())
    print(df.loc[df["Resultados"]==5])
    df.loc[df["Resultados"]==20,"Resultados"]=0
    print(df)
    df.loc[df["Concursantes"]=="Juan","Resultados"]=None
    print(df)
    
#ejercicio_1()

# EJERCICIO 2 (3)

"""
    Escribe un programa que pida dos palabras y diga si riman o no.
    Si coinciden las tres últimas letras tiene que decir que riman.
    Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
"""
def riman():
    p1 = input('introduce la primera palabra: ')
    p2 = input('introduce la segunda palabra: ')
    rimas = 0
    if p1[-1] == p2[-1]:
        if p1[-2] == p2[-2]:
            if p1[-3] == p2[-3]:
                print('Riman mucho')
            else:
                print('riman un poco')
        else:
            print('No riman')    
    else:
        print('No riman')

riman()