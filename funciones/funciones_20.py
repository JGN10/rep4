#from telnetlib import theNULL
#import pandas as pd

def generar_n_caracteres(n, caracter):
    try:
        salida = ""
        salida = caracter * n
        #for i in range(n):
        #    salida += caracter
        return (salida)
        #print(f'salida  {salida}')
    except Exception:
        return None




def procedimiento(lista):
    for i in lista:
        imprimir = ''
        imprimir = 'X' * i
        print(f'{imprimir}' )
        #for j in range(len(i)):
        #    imprimir +=



def mas_larga(lista):
    longitud = 0
    palabra = ''
    for i in lista:
        if longitud <= len(i):
            longitud = len(i)
            palabra = i
    return palabra, longitud

#x,y = mas_larga(['1','12','123'])
#print(x)
#print(y)

def filtrar_palabras(lista, n):
    lista_aux = []
    for i in lista:
        if len(i) >= n:
            lista_aux.append(i)
    return lista_aux
    print(lista_aux) 

#filtrar_palabras(['123','22','222','4444'], 4)

def c_mayusculas(cadena):
    mayusculas = 0
    cad_aux = ''
    for i in cadena:
        if i== i.upper():
            mayusculas += 1
            cad_aux += i
    return mayusculas, cad_aux

#m,c = c_mayusculas('bcdDDef')
#print(m)
#print(c)

def mayores(x):
    contador = 0
    for i in x:
        if i > 20:
            contador += 1
    print(f'El número de personas con más de 20 años es {contador}')





def main():
    try:
        nombres = []
        nombres_buscados = []
        numero = int(input('introduce el número de nombres a introducir '))
        letra = input('introduce la letra por la cual comparar ')
        cuantos = 0
        for i in range(numero):
            nombres.append(input(f'introduce el nombre {i+1} '))
        for j in nombres:
            if j.startswith(letra):
                nombres_buscados.append(j)
                cuantos += 1
        print(f'la lista de nombres encontrados que comienzan por {letra} son {cuantos} y los nombres son {nombres_buscados}')
        return nombres_buscados,cuantos
    except Exception:
        return None

#n,c = main()
#print(n)
#print(c)

def contar_vocales():
    cadena = input('introduce la cadena a comparar ')
    #df = pd.DataFrame (columns= ['vocal','numero'])
    #df_aux = pd.DataFrame
    vocales = ['A','E','I','O','U']
    numero = 0
    for i in vocales:
        numero = 0
        for j in cadena:
            if i==j.upper():
                numero += 1
        print(f'El número de {i} en la cadena {cadena} es {numero}')

#contar_vocales()







    



