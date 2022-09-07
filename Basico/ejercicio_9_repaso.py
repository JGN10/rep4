# EJERCICIO 1

"""
    Dado este listado de números:

    -3, 150, 0, 499, 500, 1200, -350, 0, 750, 25

    Haz un pequeño algoritmo que haga lo siguiente:

    Si el número es negativo debe imprimir lo siguiente el valor es negativo
    Si es 0 debe imprimir un mensaje que indique: 0
    Si se encuentra entre 0 (no incluido) y 200 (si incluido), imprime 0,200
    Si se encuentra entre 200 (no incluido) y 500 (no incluido), debe imprimir (200, 500)
    Si es 500 debe continuar sin hacer nada
    Si se encuentra entre 500 (no incluido) y 1000 (no incluido) debe saltar automaticamente y dejar de testear (parar)
    Para el resto de números, debe decir: valor demasiado grande, desde 1000, en adelante

"""

# 1) Escribir en formato lista

# 2) Haz el propio ejercicio de programación planteado

def ejercicio_1():
    listado = [-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25]
    for i in listado:
        if i < 0:
            print(f'el valor {i} es negativo')
        elif i == 0:
            print(i)
        elif (i > 0) and (i<=200):
            print ('el valor entre 0,200')
        elif (i>200) and (i<500):
            print('(200,500)')
        elif (i>500) and (i<1000):
            break
        elif i>=1000:
            print('valor demasiado grande, desde 1000, en adelante')

#ejercicio_1()

# EJERCICIO 2

# Dada la lista de nombre "listado" y de valores: 10, 20, 20, 30, 40, 40, 40

# 1) Crea la lista e imprimela

# 2) Haz un set de esa lista

# 3) Trata de buscar los números NO REPETIDOS de esa lista (sin usar set)

# Pista: Puedes almacenar todo en una nueva lista
def ejercicio_2():
    listado=[10, 20, 20, 30, 40, 40, 40]
    print(listado)
    list_aux=set(listado)
    print(list_aux)
    list_aux= []
    for i in listado:
        if i not in list_aux:
            print(f'no está {i}')
            list_aux.append(i)
    print(list_aux)


#ejercicio_2()

# EJERCICIO 3

# Dados estos clientes:

# Usando el continue/break

# Trata de averiguar si un cliente concreto se encuentra en la BBDD (Base de Datos)

# "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"

def ejercicio_3():
    bbdd=["Ana Pérez", "Juan", "Andres", "Luis", "Pedro", "Estefanía", "Alberto", "Susana", "Luis González"]
    entrada = input('introduce el nombre a buscar o 0 para finalizar ')
    encontrado = 0
    while entrada != "0":
        for i in bbdd:
            if entrada == i:
                print(f'el cliente {entrada} se ha encontrado')
                encontrado = 1
                break
                           
        if encontrado == 0:
            print(f'el cliente {entrada} NO se ha encontrado')
        encontrado = 0            
        entrada = input('introduce el nombre a buscar o 0 para finalizar ')

ejercicio_3()