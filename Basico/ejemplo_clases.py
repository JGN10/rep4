import os
import sys

script_dir = os.path.dirname( __file__ )
print(script_dir)
mymodule_dir = os.path.join( script_dir, '..', 'clases')
print(mymodule_dir)
sys.path.append( mymodule_dir )
print (sys.path)

#from cgi import print_arguments
from clase1 import *
print('dentro de clase ')
var_global = 'valor definido en el fichero clase'
x = 'xx'
y = 'yy'
x,y = clase1.funcion1(x,y)
print('despues de llamar a la clase, deben cambiar con el valor anterior')
print(f'valor de X {x}')
print(f'valor de y {y}')

