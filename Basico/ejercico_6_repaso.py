# EJERCICIO 1
listado=[30, 20, 10, 50, 40]
# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40
def ejercicio1(lista):
    minimo=lista[0]
    print(lista)
    print(type(lista))
    print(f"El mínimo de la lista es {min(lista)}")
    for i in lista:
        if minimo > i:
            minimo = i
    print(f"El mínimo de la lista (por bucles) es {minimo}")
    

#ejercicio1(listado)

# 1) Escribe el listado e ímprimelo

# 2) Prueba con min(listado)

# 3) Realiza lo mismo pero con bucles y condicionales


# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

# 2) Prueba con max(listado)

# 3) Realiza lo mismo pero con bucles y condicionales

def ejercicio2(lista):
    maximo=lista[0]
    print(lista)
    print(type(lista))
    print(f"El máximo de la lista es {max(lista)}")
    for i in lista:
        if maximo < i:
            maximo = i
    print(f"El máximo de la lista (por bucles) es {maximo}")

#ejercicio2(listado)


# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales
def ejercicio3(lista):
    print(f'listado antes del sort {lista}')
    listado_ascendente = lista.sort()
    print(f'listado ascendente con sort  {lista}')

def ejercicio3_bucle(lista):
    print(f'listado antes del bucle {lista}')
    listado_ascendente = []
    for i in range(0,len(lista)):
        minimo = lista[0]
        for j in lista:
            if minimo > j:
                minimo = j
        lista.remove(minimo)
        listado_ascendente.append(minimo)

    print(f'listado ascendente con bucle {listado_ascendente}')

listado2 = listado.copy()
ejercicio3(listado)    
#print(listado)
#print(listado2)
ejercicio3_bucle(listado2)
#print(listado2)


# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales
def ejercicio4(lista):
    print(f'listado antes del sort {lista}')
    listado_descendente = lista.sort(reverse=True)
    print(f'listado descendente con sort {lista}')

def ejercicio4_bucle(lista):
    
    print(f'listado antes del bucle {lista}')
    listado_descendente = []
    for i in range(0,len(lista)):
        maximo = lista[0]
        for j in lista:
            if maximo < j:
                maximo = j
        lista.remove(maximo)
        listado_descendente.append(maximo)

    print(f'listado descendente con bucle {listado_descendente}')

listado=[30, 20, 10, 50, 40]
listado2 = listado.copy()
ejercicio4(listado)    
ejercicio4_bucle(listado2)



# EJERCICIO 5
"""
    Pendiente
"""