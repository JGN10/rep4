import pandas as pd

# Ejercicio 1

"""
    Desarrolla el siguiente ejercicios de POO:

   * Alumnos  -> Es la clase.
   * __init__ -> Es el método init
   * nombre, edad, asignatura y nota son las propiedades
   * Instanciamos..
   * los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
   * y el.__init__ los inicializa

   A continuación muestra la edad del alumno 2 y el alumno 3 y sus notas
"""
class alumnos():

    def __init__(self, nombre, edad, asignatura, nota):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura
        self.nota = nota

alumno1 = alumnos('nombre1',1, 'asignatura1', 11)
alumno2 = alumnos('nombre2',2, 'asignatura2', 22)
alumno3 = alumnos('nombre3',3, 'asignatura3', 33)

#print(alumno2.edad)
#print(alumno3.edad)
#print(alumno3.nota)

"""
class Alumnos:

    def __init__(self, nombre, edad, asignatura, nota):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura
        self.nota = nota

alumno1 = Alumnos("Pedro", 25, "Matemáticas", 6.8)
alumno2 = Alumnos("Elia", 26, "Historia", 7.4)
alumno3 = Alumnos("Sergio", 28, "Lengua", 9.7)

print(alumno2.edad)
print(alumno3.edad)
print(alumno1.nota)
print(alumno2.nota)
print(alumno3.nota)
"""

# Ejercicio 2

"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
def imprime_edad():
    edad = int(input('introduce la edad '))
    for i in range(1,edad+1):
        print(f'Ha cumplido {i} años')

#imprime_edad()


def edad():
    age = int(input("¿Cuántos años tienes? "))
    for i in range(age):
        print("Has cumplido " + str(i+1) + " años")

#edad()

# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
def letras_inversa():
    palabra = str(input('introduce la palabra a invertir :'))
    for i in range (1,len(palabra)+1):
        print(palabra[i*-1])
    
#letras_inversa()



def palabra():
    word = input("Introduce una palabra: ")
    for i in range(len(word)-1, -1, -1):
        print(word[i])

#palabra()

# Ejercicio 4

"""
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces,
    una con todas las letras minúsculas,
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
def imprimir_nombre():
    nombre = str(input('introduce el nombre completo'))
    print(nombre.upper())
    print(nombre.lower())
    print(nombre.title())

#imprimir_nombre()

def nombre_completo():
    name = input("¿Cómo te llamas? ")
    print(name.lower())
    print(name.upper())
    print(name.title())

#nombre_completo()

# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""

def imprime_telefono():
    telefono = str(input('introduce el número con formato +xx-xxxxxxxxx-xx: '))
    print(f'prefijo {telefono.split("-")[0]}')
    print(f'número {telefono.split("-")[1]}')
    print(f'Extensión {telefono.split("-")[2]}')

#imprime_telefono()

def opcion1():
    tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
    print('El número de teléfono es ', tel[4:-3])

def opcion2():
    tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
    print('El número de teléfono es ', tel.split("-")[1])

#opcion1()
#opcion2()


# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
    y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
    ejemplo geranio --> e --> gEranio
"""
def cambia_vocal(opcion):
    frase_aux = ""
    frase = str(input('introduce la frase a cambiar'))
    vocal = str(input('introduce la vocal '))
    if opcion == 1:
        for i in frase:
            if i == vocal:
                frase_aux = frase_aux + i.upper()
            else:
                frase_aux = frase_aux + i
    else:
        frase_aux = frase.replace(vocal,vocal.upper())
    print(frase)    
    print(frase_aux)

#cambia_vocal(2)



def frase():
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal en minúscula:  ")
    print(frase.replace(vocal, vocal.upper()))

#frase()

# Ejercicio 7

"""
    Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
    Ejemplo: 24.75 --> 24 Euros con 75 Centimos
"""
def divide_precio(opcion):

    precio = str(input('introduce el numero con decimales: '))
    if opcion == 1:
        entero = int(precio)
        decimal =int((precio - entero) * 100)
    else:
        entero = precio.split(".")[0]
        decimal = precio.split(".")[1]


    print (f'precio {entero} € con {decimal} centimos ')

#divide_precio(2)

def precio():
    precio = input("Introduce el precio del producto con dos decimales:  ")
    print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

#precio()

# otra opción...

def precio1():
    precio = input("Introduce el precio del producto con dos decimales:  ")
    print(precio.split(".")[0], 'euros y', precio.split(".")[1], 'céntimos.')

#precio1()

# Ejercicio 8



"""
    Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

    Mes Ventas Gastos

    Enero 30500 22000

    Febrero 35600 23400

    Marzo 28300 18100

    Abril 33900 20700
"""

def imprime_dataframe(opcion):
    if opcion == 1:
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril']
        ventas = [30500, 35600, 28300, 33900]
        gastos = [22000, 23400, 18100, 20700]
        datos = pd.DataFrame()
        datos['Meses'] = meses
        datos['ventas'] = ventas
        datos['gastos'] = gastos
        print(datos)
    else:
        dic1 = {"meses":['Enero', 'Febrero', 'Marzo', 'Abril'],
            'Ventas':[30500, 35600, 28300, 33900],
            'Gastos':[22000, 23400, 18100, 20700]
            }
        datos2 = pd.DataFrame(dic1)
        print(datos2)
        return datos2

datos1 = imprime_dataframe(2)


def data():
    datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'],
            'Ventas':[30500, 35600, 28300, 33900],
            'Gastos':[22000, 23400, 18100, 20700]}
    contabilidad = pd.DataFrame(datos)
    print(contabilidad)
    return contabilidad

#contabilidad = data()
#contabilidad1 = data()

# Ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
"""
def imprime_balance(datos, paises):
    pais = []
    lista = []
    for i in paises:
        pais.append(i)
        pais.append(list(datos[datos["meses"]==i].Ventas - datos[datos["meses"]==i].Gastos)[0])
        lista.append(pais)
        pais = []
    print(lista)
    total = 0
    for i in lista:
        print(f'el balance del mes {i[0]} es el valor {i[1]}')
        total = total + i[1]
    print(f'el balance total {total}')
    
    

    
#imprime_balance(datos1,['Febrero','Abril'])


#venta1 = datos1[datos1['meses']=='Enero'].Ventas - datos1[datos1['meses']=='Enero'].Gastos
#print(list(venta1)[0])

#print(datos1[datos1['meses']=='Enero'].Ventas)




def balance(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()

#print(balance(contabilidad, ['Enero','Marzo']))

# otra opción...

def balance2(contabilidad, meses):
    # creamos la columna balance:
    contabilidad1["Balance"] = contabilidad1["Ventas"] - contabilidad["Gastos"]

    # creamos una lista vacia con los index de los meses
    list_index = []
    for i in range(len(meses)):
        index = contabilidad.index[contabilidad['Mes'] == meses[i]].tolist()[0]
        list_index.append(index)

    # creamos una lista con los balances de cada mes
    value_balance = []
    for value in list_index:
        balance = contabilidad["Balance"][value]
        value_balance.append(balance)

    # sumatorio de esos balances
    resultado = sum(value_balance)
    return resultado

#print(balance(contabilidad1, ['Enero','Marzo']))
#print(balance(contabilidad1, ['Enero','Marzo','Abril']))


# Ejercicio 10

"""
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
    pregunte al usuario la nota que ha sacado en cada asignatura,
    y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
"""
def asignaturas():
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas=[]
    for i in materias:
        nota = input(f'Introduce la nota de la asignatura {i}: ')
        notas.append(nota)
    contador = 0
    for i in materias:
        print(f'La nota para la asignatura {i} es {notas[contador]}')
        contador += 1
    
asignaturas()




def subjects():
    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    scores = []
    for subject in subjects:
        score = input("¿Qué nota has sacado en " + subject + "?")
        scores.append(score)
    for i in range(len(subjects)):
        print("En " + subjects[i] + " has sacado " + scores[i])

#subjects()