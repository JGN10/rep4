# Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""
def inversa(cadena):
    resultado = ''
    for i in range(1,len(cadena)+1):
        resultado = resultado + cadena[i*(-1)]
    print(resultado)

inversa('1234567890')
"""


def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

print(inversa("Hola mundo"))

# Otra opción..

def inversa2(cadena):
    return cadena[::-1]

resultado = inversa2("Hola mundo2")
print(resultado)

"""

# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo 
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""

def palindromo(valor):
    mitad = int(len(valor)/2 + 1)
    for i in range(1,mitad):
        if valor[i-1] != valor[i*(-1)]:
            return "no es palíndromo"
    return "Es palíndromo"

print(palindromo('12354321'))
"""
def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False

cadena = input("introduce una letra por favor: ")

print(palindromo(cadena))

# otra opción...
def es_palindromo(cadena):
    palabra_invertida = inversa(cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print("No es palindromo")
            break
    if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
        print("Es palindromo") # es porque recorrió todo el ciclo for y todas las
                                            # letras son iguales

es_palindromo("radar")
"""
# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos 1 elemento en común o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""

def superposicion (valor1, valor2):
    for i in valor1:
        for j in valor2:
            if i==j:
                return True
    return False

print(superposicion('1234','897770'))
print(superposicion([1,2,3],[5,6,3]))

"""
def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

lista1 = [1, 2, 3]
lista2 = [1, 4, 8]

print("Resultado superposicion 1: ", superposicion(lista1, lista2))

lista1 = [0, 2, 3]
lista2 = [1, 4, 8]

print("Resultado superposicion 2: ", superposicion(lista1, lista2))
"""
