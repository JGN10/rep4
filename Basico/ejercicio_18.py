
import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'funciones')
print(mymodule_dir)
sys.path.append( mymodule_dir )

#import Ejercicios_18_Repaso
from funciones import *

#Ejercicios_18_Repaso.suma([2, 3])

while True:
    try:
        print('\n')
        ejercicio = int(input('introduce el número del ejercicio que quieres ejecutar (0 para finalizar) '))
        if ejercicio in [1, 2, 3, 4, 5]:
            if ejercicio == 1:
                valor1 =int(input('introduce el primer número a comparar '))
                valor2 = int(input('introduce el segundo número a comparar '))
                result = maximo(valor1, valor2)
                if result != None:
                    print (f'el valor mayor es {result} ')
                else:
                    print('los valores introducidos no son correctos ')
            elif ejercicio == 2:
                valor1 = int(input('introduce el primer número a comparar '))
                valor2 = int(input('introduce el segundo número a comparar '))
                valor3 = int(input('introduce el tercer número a comparar '))
                result = max_de_tres(valor1, valor2, valor3)
                if result != None:
                    print (f'el valor mayor es {result} ')
                else:
                    print('los valores introducidos no son correctos ')             
            elif ejercicio == 3:
                valor1 = input('introduce la lista o cadena ')
                if valor1[0]=="[":
                    valor1 = eval(valor1)
                result = longitud(valor1)
                print (f'la longitud de la cadena es  {result} ')
            elif ejercicio == 4:
                valor1 = input('introduce el carácter a comparar ')
                result = es_vocal(valor1)
                if result:
                    print(f'El carácter {valor1} es vocal ')
                else:
                    print(f'El carácter {valor1} NO es vocal ')
            elif ejercicio == 5:
                valor1 = input('introduce la cadena a utilizar ') 
                valor1 = eval(valor1)
                result = suma_lista(valor1)
                if result != None:
                    print(f'El valor de la suma de la lista {valor1} es {result} ')
                else:
                    print(f'La lista {valor1} tiene valores no enteros ')

                result = mult_lista(valor1)
                if result != None:
                    print(f'El valor de la multiplicación de la lista {valor1} es {result} ')
                else:
                    print(f'La lista {valor1} tiene valores no enteros ')           
        elif ejercicio == 0:
            break
    except Exception:
        print('error al introducir los datos')
        break        
    


