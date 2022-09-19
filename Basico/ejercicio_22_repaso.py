# EJERCICIO 1

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
    Escribir una tercera función que reciba un diccionario con los precios
    y porcentajes de una cesta de la compra, y una de las funciones anteriores, 
    y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
    Ejemplo de diccionario: {1000:20, 500:10, 100:1}
"""
#from xmlrpc.server import _DispatchArity1


def descuento(valor,descuento):
    resultado = valor - (valor * descuento) / 100
    return resultado

def IVA(valor,incremento):
    resultado = valor + (valor * incremento) /100
    return resultado

def cesta(lista,funcion):
    resultado = 0
    for clave,valor in lista.items():
        resultado += funcion(clave,valor)
    print(f"el valor de la cesta es {resultado}")

#cesta({1000:20, 500:10, 100:1}, descuento)
#cesta({1000:20, 500:10, 100:1}, IVA)

def apply_discount(price, discount):
    '''
    Función que aplica un descuento a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el descuento.
        discount: Es el porcentaje a descontar.
    Devuelve:
        El precio final tras aplicar el descuento.
    '''
    return price - price * discount / 100
    
def apply_IVA(price, percentage):
    '''
    Función que aplica un IVA a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el IVA.
        percentage: Es el porcentaje del IVA a aplicar.
    Devuelve:
        El precio final tras aplicar el IVA.
    '''
    return price + price * percentage / 100

def price_basket(basket, function):
    '''
    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
    Parámetros:
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    '''
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

#print('El precio de la compra tras aplicar los descuentos es: ', price_basket({1000:20, 500:10, 100:1}, apply_discount))
#print('El precio de la compra tras aplicar el IVA es: ', price_basket({1000:20, 500:10, 100:1}, apply_IVA))

# EJERCICIO 2

"""
    Escribir una función que reciba otra función y una lista,
    y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista.
"""

def multiplica(valor):
    return (valor * 10)

def funcion_dinamica(lista,funcion):
    lista_aux = []
    for i in lista:
        lista_aux.append(funcion(i))
    return lista_aux

#print(funcion_dinamica([1,2,3,4],multiplica))


def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n * n

#print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))

# EJERCICIO 3

"""
    Escribir una función que reciba una frase y
    devuelva un diccionario con las palabras que contiene y su longitud.
    Ejemplo: "Hola Mundo" --> {"Hola": 4, "Mundo": 5}
"""

def diccionario_palabras(lista):
    dic1={}
    for i in lista.split():
        dic1[i] = len(i)
    return dic1

#print(diccionario_palabras("1 12 123 1234, 12345, 123456 1234567"))


def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    words = sentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

#print(length_words('Welcome to Python'))

# otra opción...

def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    return {word:len(word) for word in sentence.split()}

#print(length_words('Welcome to Python'))

# EJERCICIO 4

"""
    Escribir una función reciba una lista de notas y
    devuelva la lista de calificaciones correspondientes a esas notas.
    Suspenso < 5
    Aprobado = 5
    Suficiente entre 5 - 7
    Notable 7-9
    Sobresaliente > 9
"""
def notas(valor):
    if valor < 5:
        return "Suspenso"
    elif valor == 5:
        return "Aprobado"
    elif (valor > 5) and (valor <=7):
        return "Suficiente"
    elif (valor > 7) and (valor <=9):
        return "Notable"
    elif (valor > 9):
        return "Sobresaliente"

#print( list(map(notas,[6.5,3,5,7,8,9,9.5])))


def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        scores: Es una lista de valores reales entre 0 y 10.
    Devuelve
        La lista de calificaciones correspondiente a las notas de scores.
    '''
    return list(map(grade, scores))

#print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))

# EJERCICIO 5

"""
    Escribir una función que reciba un diccionario con las asignaturas y
    las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas
    y las calificaciones correspondientes a las notas.
"""

def cambia_notas(valor):
    dic1={}
    for asignatura,nota in valor.items():
        print(asignatura)
        print(nota)
        dic1[asignatura.upper()] = notas(nota)
    print(dic1)

#cambia_notas({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10})

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
    return dict(zip(subjects, grades))

#print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))

# Otra opción...

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    return {subject.upper():grade(score) for subject, score in scores.items()}

#print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))

# EJERCICIO 6

"""
    Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
    pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
    por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def valida_pass():
    clave = str(input('introduce la contraseña original'))
    clave_aux = str(input('introduce la contraseña a validar'))
    if clave == clave_aux:
        print('las contraseñas son iguales')
    else:
        print('las contraseas no son iguales')

valida_pass()


def password():
    key = "contraseña"
    password = input("Introduce la contraseña: ")
    if key == password.lower():
        print("La contaseña coincide")
    else:
        print("La contraseña no coincide")

#password()