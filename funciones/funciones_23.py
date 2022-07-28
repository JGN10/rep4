


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
from matplotlib.cbook import print_cycles


class Alumnos:
    
    def __init__(self, nombre, edad, asignatura, nota):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura
        self.nota = nota

    def imprime_alumno(self):
        print('los datos del alumno son: ')
        print(f'El nombre es {self.nombre}')
        print(f'La edad es {self.edad}')
        print(f'La asignatura es {self.asignatura}')
        print(f'La nota es {self.nota}')

            

alumno1 = Alumnos('Marta',10,'Matemáticas',5.5)
alumno2 = Alumnos('Juan',12,'Física',8.3)
alumno3 = Alumnos('Paco',7,'Quimica',3.7)
'''alumno1.imprime_alumno()
alumno2.imprime_alumno()
alumno3.imprime_alumno()
'''

# Ejercicio 2
"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
def imprime_años():
    alumno=int(input('introduce el número del alumno a mostrar sus años cumplidos '))
    if alumno == 1:
        edad = alumno1.edad
    elif alumno == 2:
        edad = alumno2.edad
    elif alumno == 3:
        edad = alumno3.edad
    for i in range(edad):
        print(f'Ha cumplido {i+1} años')

#imprime_años()
        



# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
def imprime_inversa():
    cadena = input('introduce la cadena a mostrar su inversa ')
    cadena_for = '' 
    for i in range(len(cadena),0,-1):
        cadena_for += cadena[i-1]
    print(f'la cadena inversa con el for es : {cadena_for}')
    print(f'la cadena inversa con una instruccion es {cadena[::-1]}')

   
#imprime_inversa()
        

# Ejercicio 4

"""
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces,
    una con todas las letras minúsculas,
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
def imprime_nombre():
    nombre = str(input('introduce el nombre completo '))
    nombre_for_upper = ''
    nombre_for_lower = ''
    nombre_for_title = ''
    nombre_upper = nombre.upper()
    nombre_lower = nombre.lower()
    nombre_title = nombre.title()
    print(f' MAYUSCULAS {nombre_upper}')
    print(f' minúsculas {nombre_lower}')
    print(f' Primera mayúsculas {nombre_title}')
    for i in range(len(nombre)):
        nombre_for_upper += nombre[i].upper()
        nombre_for_lower += nombre[i].lower()
        if i == 0 and nombre[i] != ' ':
            nombre_for_title += nombre[i].upper()
        elif nombre[i-1] == ' ' and nombre[i] != ' ':
            nombre_for_title += nombre[i].upper()
        else:
            nombre_for_title += nombre[i].lower()
    print(f' MAYUSCULAS {nombre_for_upper}')
    print(f' minúsculas {nombre_for_lower}')
    print(f' Primera mayúsculas {nombre_for_title}')    
        


#imprime_nombre()

# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
def imprime_telefonos():
    telefono = str(input('introduce el número de teléfono con formato adecuado '))
    lista_telf = telefono.split('-')
    if len(lista_telf) == 3:
        print(f'el número de teléfono es {lista_telf[1]}')
        print(f'La extensión del teléfono es {lista_telf[2]}')
    else:
        Print('Formato de teléfono erróneo')   
    

#imprime_telefonos()


# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
    y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
def cambia_vocal():
    cadena = str(input('introduce la cadena '))
    letra = str(input('introduce la letra a cambiar '))
    if letra == 'a':
        tilde = 'á'
    elif letra == 'e':
        tilde = 'é'
    elif letra == 'i':
        tilde = 'í'
    elif letra == 'o':
        tilde = 'ó'
    elif letra == 'u':
        tilde = 'ú'    
        
    cadena_cambiada = cadena.replace(letra,letra.upper())
    cadena_cambiada = cadena_cambiada.replace(tilde,tilde.upper())
    print(f'la cadena cambiada es : {cadena_cambiada}')
    

#cambia_vocal()

# Ejercicio 7

"""
    Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
def parte_entera():
    precio = float(input('introduce el precio con valores decimales'))
    entero = int(precio)
    decimal = (precio-entero)*100
    print (f'el numero entero es {entero}')
    print (f'la parte decimal pero en entero {int(decimal)}')
    print (f'la parte decimal pero en decimal {round(decimal,1)}')

#parte_entera()



# Ejercicio 8
"""
    Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

    Mes Ventas Gastos

    Enero 30500 22000

    Febrero 35600 23400

    Marzo 28300 18100

    Abril 33900 20700
"""

def leer_datos_csv():
    import pandas as pd
    datos = pd.read_csv("C:/jero/Curso Data Science2/repositorio/rep4/ejercicio_8.csv", sep=';' )
    print(datos.head())

#leer_datos_csv()

# Ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
"""

def imprime_balance(lista,df_meses):
    balance_total = 0
    Balance_mes = 0
    for i in lista:
        ventas = int(df_meses.loc[df_meses['Mes'] == i, 'Ventas'])
        gastos = int(df_meses.loc[df_meses['Mes'] == i, 'Gastos'])
        balance_mes = ventas - gastos
        balance_total += balance_mes
        print(f'El balance para el mes {i} es: {balance_mes}')
    print(f'El balance total para los meses indicados es: {balance_total}')


def carga_df():
    import pandas as pd
    datos = pd.read_csv("C:/jero/Curso Data Science2/repositorio/rep4/ejercicio_8.csv", sep=';' )
    return datos

#lista_meses=['Enero','Marzo','Abril']
#ventas = carga_df()
#imprime_balance(lista_meses,ventas)

# Ejercicio 10

"""
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
    pregunte al usuario la nota que ha sacado en cada asignatura,
    y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.

"""
def introduce_asignaturas ():
    listado=[]
    print('introduce las asignaturas ( 0 para finalizar) ')
    i = 1
    while True:
        asignatura = input(f'introduce la asignatura {i} ')
        if asignatura == '0':
            break
        else:
            listado.append(asignatura)
            i += 1
    return listado

def introduce_notas(lista):
    dict ={}
    for i in lista:
        dict[i] = int(input(f'introduzca la nota para la asignatura {i} '))
    return dict

def imprime_notas(dict):      
    for asignatura,nota in dict.items():
        print(f'Has sacado para la asignatura de {asignatura} la nota de {nota} ')





#lista = introduce_asignaturas()
#dict = introduce_notas(lista)
#imprime_notas(dict)


'''
class alumno():

    def __init__(self,nombre):
        self.nombre=nombre

    def imprime(self):
        print(f'nombreeee : {self.nombre}' )

alumno1=alumno('pepe')
alumno2=alumno('paco')
alumno3=alumno('qq')

for i in range(1,4,1):
    cadena = "alumno" + str(i)
    cadena.imprime()

    

'''