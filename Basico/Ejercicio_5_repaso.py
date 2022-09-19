import os
import sys
import numpy as np

script_dir = os.path.dirname( __file__ )
#print(script_dir)
mymodule_dir = os.path.join( script_dir, '..', 'funciones')
#print(mymodule_dir)
sys.path.append( mymodule_dir )
#print (sys.path)
from funciones_5_repaso import *

# EJERCICIO 1

# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1.
    # Usa las formas que conozcas para crearla y el uso de type para asegurarte de que es una lista.
test = [25,8,32,1]
print(test)
print(type(test))    
test2 =list((25,8,32,1))
print(test2)
print(type(test2))
arr=np.array([25,8,32,1])
test3=arr.tolist()
print(test3)
print(type(test3))

# b) Apendiza un valor de valor 20, 32, 25, 32
test = f5_apendiza_valor(test,20)
print(test)
test = f5_apendiza_valor(test,32)
print(test)
test = f5_apendiza_valor(test,25)
print(test)
test = f5_apendiza_valor(test,32)
print(test)


# c) Elimina el valor 8 de la lista
test4 = test
test.remove(8)
print(test)
print(test4)

# d) Elimina los duplicados que haya en la lista test
test = set(test)
print(test)
print (type(test))
test = list(test)
print(type(test))


# e) Crea una segunda lista de nombre "info" que contenga los valores:
    #  25, 100, 10, 20, 5, 25, 30, 200
info =([25, 100, 10, 20, 5, 25, 30, 200])
print(info)

# f) ¿Cuántos valores se repiten entre las listas?
cuantos = 0
for i in test:
  for y in info:
    if i==y:
      print(f"se repite el valor {i}")
      cuantos += 1
print(f"se repiten {cuantos} valores")
# g) Muéstrame el maximo y mínimo en las dos listas
print(max(test))
print(min(test))
print(max(info))
print(min(info))

# h) Crea una nueva variable de nombre "matriz" transformando la lista test en matriz
matriz = np.array(test)
print(matriz)
print(type(matriz))

# i) Crea una función que se llame "funcion_división" donde se divida
    # el test con valor 32 entre info con valor 5 y muestra el resto de la división
f5_funcion_division(test,0,info,4)



# j) Con ayuda de reverse() muestra la inversa de test
print(test)
print(test.reverse())
print(test)

# k) Con el listado info utiliza un bucle for con la ayuda de enumerate(),
    # para mostrar posición y valor y crea un diccionario de nombre "newDict"
newdic={}
for i in enumerate(info):
  print ( f"posicion {i[0]}")
  print ( f"valor {i[1]}")
  newdic[i[0]] = i[1]
print(newdic)
  

# l) Crea un nuevo listado con nombre "info2" donde los valores: 25 se sustituya por "María",
    # el valor 20 por "Juan" y el valor 10 por "Pedro"
info2=[]
for i in info:
  if i == 25:
    info2.append('María')
  elif i == 20:
    info2.append('María')
  elif i == 10:
    info2.append('Pedro')
  else:
    info2.append(i)

print(info2)

# m) Sustituye en el listado test los multiplos de 2 por "Dos"



# EJERCICIO 2

"""
    Escribe un programa que imprima los números desde 1 hasta 100

    Pero:

    * Para los múltiplos de 3 escribe "Hello"
    * Para los múltiplos de 5 escribe "World"
    * Para los múltiplos de ambos (3 y 5) escribe "Hello World"
    (en vez de los números correspondientes)
"""