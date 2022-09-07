import numpy as np

# EJERCICIO 1

# Crea una matriz con ayuda numpy:

# 1) Cuya matriz contenga 4 filas por 4 columnas de ceros

# 2) Apartir de la matriz de ceros crea la matriz identidad
def ejercicio_1():
    ceros=np.zeros((4,4))
    print(ceros)
    for i in range(len(ceros)):
        ceros[i][i]=1
    print(ceros)

#ejercicio_1()


# EJERCICIO 2

# Crea una matriz con ayuda numpy:

# Primera fila contenga: 3, 6, 8
# Segunda fila contenga: 20, 5, 7
# Tercera fila contenga: 10, 14, 1
def ejercicio_2():
    a = np.array([
        [3, 6, 8],
        [20, 5, 7],
        [10, 14, 1]
        ])
    print(a)
    print(f'el tamaño de la matriz es {a.size} ')
    print(f'las dimensiones de la matriz son {a.shape}')
    print(f'tiene algún valor 0? {0 in a}')
    print(f'tiene algún valor mayor que 10? {np.any(a>10)}')
    print(f'tiene algún valor 7? {7 in a}')
    print('matriz con unica dimensión (ravel)')
    b=np.ravel(a)
    print(b)
    print('matriz con unica dimensión con bucles')
    b=[]
    for fila in a:
        for columna in fila:
            b.append(columna)
    b = np.array(b)
    print(b)
    print(type(b))
    print('matriz con unica dimensión y elevado al cubo utilizando flatten')
    c = a.flatten()
    print(c**3)


    
  

ejercicio_2()

# 1) Crea la transpuesta de esta matriz

# 2) Muestra el tamaño de la matriz

# 3) Muestra las dimensiones

# 4) ¿La matriz tiene valores menores de 0?

# 5) ¿La matriz tiene algún valor mayor de 10?

# 6) Coge una muestra de 5 valores de esa matriz usando linespace

# 7) La matriz contiene el valor 7

# 8) Crea una copia de esa matriz en una única dimensión

# 9) Crea una copia de esa matriz en una única dimensión, en este caso usando un bucle y una lista vacia

# 10) Realiza a esta última matriz creada con flatten la potencia de 3