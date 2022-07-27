#import pandas as pd

def es_bisiesto(x):
    if (x % 4 == 0) and (( x % 100 != 0) or (x % 400 == 0)):
        return True
    else:
        return False

#print(es_bisiesto(2022))

def calcula_capital():
    capital_inicial = float(input('introduzca el capital '))
    interes = float(input('introduzca el interés '))
    anios = int(input('introduzca el número de años '))
    capital = capital_inicial
    for i in range(anios):
        capital += (capital * interes)/100
        print(f'El capital para el año {i+1} es {round(capital,2)}')
    return capital_inicial, interes, anios, capital

calcula_capital()

def calcula_precio():
    pelis = pd.DataFrame()
    peliculas = {
        'PRECIO' : [2.50, 3.00, 3.50, 4.00],
        'CATEGORIA' : ['FAVORITOS', 'NUEVOS', 'ESTRENOS', 'SUPER ESTRENOS'],
        'CODIGO' : [1, 2, 3, 4],
        'RECARGO/DIA DE ATRASO' : [0.50, 0.75, 1.00, 1.50]
    }
    pelis = pd.DataFrame(peliculas)
    print (pelis)
    #print(pelis[pelis["CODIGO"] == 2])
    #print(pelis[pelis["CODIGO"] == 2]["CATEGORIA"])
    #V1=str(pelis[pelis["CODIGO"] == 2]["CATEGORIA"])
    #print(V1)

    #print (pelis.dtypes)
    #pelis2 = pelis['CATEGORIA'].astype(str)
    #print (pelis2.dtypes)
    codigo = int(input('introduzca el código de la categoria '))
    precio = float(pelis.loc[pelis['CODIGO'] == codigo, 'PRECIO'])
    recargo = float(pelis.loc[pelis['CODIGO'] == codigo, 'RECARGO/DIA DE ATRASO'])
    catego = str(pelis.loc[pelis['CODIGO'] == codigo, 'CATEGORIA'])
    #print(catego)
    dias = int(input('introduzca el numero de días de retraso '))
    calculo = precio + (recargo * dias)
   
    print (f'el valor a pagar para el código {codigo} y para los días de retraso {dias} es {calculo}')
'''
#print(pelis)
    #pelis  = pelis.set_index('CODIGO', drop=False)
    #pelis  = pelis.set_index('CODIGO')
    #print (pelis[pelis['CODIGO' == codigo]])
    #precio = float(pelis.loc[pelis.index[codigo], 'PRECIO'])

'''





#calcula_precio()

