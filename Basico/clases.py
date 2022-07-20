from cgi import print_arguments
from clase1 import *
print('dentro de clase ')
var_global = 'valor definido en el fichero clase'
x = 'xx'
y = 'yy'
clase1.funcion1(x,y)
print('despues de llamar a la clase')
print(f'valor de X {x}')
print(f'valor de y {y}')

