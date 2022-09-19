"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
def generar_n_caracteres():
    caracter = str(input('Introduce la letra a duplicar'))
    veces = int(input('introduce el número de veces a repetir la letra'))
    cadena = ""
    for i in range(veces):
        cadena = cadena + caracter
    return cadena

#print(f"la cadena duplicada es {generar_n_caracteres()}")



"""
def generar_n_caracteres(n, caracter):
    return n * caracter

print(generar_n_caracteres(5, 'x'))
"""

# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""
def procedimiento(valor):
    for i in valor:
        print("X"*i)

#procedimiento([6,7,5,4,8,9])

"""
def procedimiento(lista):
    for i in lista:
        print(i * "x")

procedimiento([4, 9, 7])
"""

# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(valor):
    largo = 0
    palabra = ''
    for i in valor:
        if largo < len(i):
            largo = len(i)
            palabra = i
    return palabra, largo

#p1,l1 = mas_larga(['123456', '123','1234567890', '123456'])
#print(f'la palabra mas larga es {p1}')


"""
def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

print(mas_larga(["coche", "tortuga", "bici"]))
"""
# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista,numero):
    cadenas= []
    for i in lista:
        if len(i) > numero:
            cadenas.append(i)
    return cadenas

#print(filtrar_palabras(['12345','123','xxx','ccccc'],4))

"""
def filtrar_palabras(lista, n):
    for i in lista:
        if len(i) > n:
            print(i)

filtrar_palabras(["coche", "tortuga", "bici"], 4)
"""
# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""
def cuenta_mayusculas(valor):
    contador = 0
    for i in valor:
        if i.upper() == i:
            contador += 1
    return contador

#print(f'el número de mayúsculas de la cadena AAAxxxxZZZZ es {cuenta_mayusculas("AAAxxxxZZZZ")}')
"""
def c_mayusculas(cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minúsculas
            cont += 1
    print("La cadena tiene", cont, "mayuscula/s")

c_mayusculas("Mas que Coches")
"""
# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""
def compara_edad(valor,edad):
    for i in valor:
        if i > edad:
            print(i)

#compara_edad((10,11,23,24,67,1,10),20)


"""
def mayores(tup):
    cont = 0
    for i in tup:
        if i > 20:
            cont += 1
    print("Hay", cont, "numeros mayores a 20")
    
mayores((15, 20, 16, 31, 40, 50, 11, 13, 48, 60))
"""
# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""
def filtra_nombres(lista):
    letra = str(input('introduce la letra a comparar'))
    for i in lista:
        if i[0].upper() == letra.upper():
            print(i)
#filtra_nombres(['abc','dca','ttta','A1','A2'])
"""
def main():
    x = int(input("Cuantos nombres quieres ingresar?: "))
    lista = []
    for i in range(x):
        a = input("Ingresa el nombre: ")
        lista.append(a)   
    print("\n")
    
    comienzo = input("Con que letra empieza el nombre?: ")
    cont = 0
    for i in lista:
        if i[0] == comienzo.lower() or i[0] == comienzo.upper() :
            cont += 1
    return cont

main()
"""
# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

def cuenta_vocales():
    palabra = str(input('introduce la palabra a comparar'))
    a,e,i,o,u = 0,0,0,0,0
    vocales = "AEIOU"
    for j in palabra:
        if j.upper() == "A":
            a += 1
        if j.upper() == "E":
            e += 1
        if j.upper() == "I":
            i += 1
        if j.upper() == "O":
            o += 1
        if j.upper() == "U":
            u += 1
    return a,e,i,o,u
"""    
a1,e1,i1,o1,u1 = cuenta_vocales()
print(f'el número de a es : {a1}')
print(f'el número de e es : {e1}')
print(f'el número de i es : {i1}')
print(f'el número de o es : {o1}')
print(f'el número de u es : {u1}')
"""


"""
def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"

    for x in vocales:
        contador = 0
        for i in cadena:
            if i == x:
                contador += 1
        print("Hay %d %s." % (contador, x))

contar_vocales("Hola Mundo")
"""