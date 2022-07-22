import os
import sys

script_dir = os.path.dirname( __file__ )
#print(script_dir)
mymodule_dir = os.path.join( script_dir, '..', 'funciones')
#print(mymodule_dir)
sys.path.append( mymodule_dir )
#print (sys.path)
from funciones_19 import *

while True:
    try:
        print('\n')
        ejercicio = int(input('introduce el número del ejercicio que quieres ejecutar (0 para finalizar) '))
        if ejercicio in [1, 2, 3]:
            if ejercicio == 1:
                valor1 = input('introduce la cadena a imprimir la inversa ')
                result = inversa(valor1)
                if result != None:
                    print (f'La cadena {valor1}, dada la vuelta es: {result} ')
                else:
                    print('Algún error se ha producido ')
            elif ejercicio == 2:
                valor1 = input('introduce la primera cadena a comparar ')
                                
                result = es_palindromo(valor1)
                if result :
                    print (f'las cadena pasada son palíndromos')
                else:
                    print ('Las cadenas pasadas NO son palíndromos')
                    
                        
            elif ejercicio == 3:
                valor1 = input('introduce la primera lista ')
                if valor1[0]=="[" or valor1[0]=="(":
                    valor1 = eval(valor1)
                valor2 = input('introduce la segunda lista ')
                if valor2[0]=="[" or valor2[0]=="(":
                    valor2 = eval(valor2)
                    
                result = superposicion(valor1,valor2)
                if result:
                    print('las dos cadenas tienen al menos un valor repetido')
                else:
                    print('las dos cadenas no tienen ningún valor repetido')
            
        elif ejercicio == 0:
            break
    except Exception:
        print('error al introducir los datos')
        break        
    


