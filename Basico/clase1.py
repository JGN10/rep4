class clase1:
    
    def funcion1(x,y):
        #global var_global
        var_global = 'no es global'
        print('dentro de clase1.funcion1')
        print(f'el valor de var_global es {var_global}')
        print(f'el valor de x es {x} ')
        print(f'el valor de y es {y} ')
        x = 'cambiado dentro de funcion1 xxx'
        y = 'cambiado dentro de funcion1 yyy'
        print(f'el valor de x despues de cambiarlo es {x} ')
        print(f'el valor de y despues de cambiarlo es {y} ')
        return('aa','bb')


