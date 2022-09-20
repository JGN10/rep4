# EJERCICIO 1
"""
    1) Crea el siguiente programa:

    Una clase de nombre Librería
    Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería.
    En esta clase Rosalia, crea una función "result" cuyo resultado sea los datos de los libros.
    declara los Objetos siguientes:
    libro1 --> Oceanarium, Ciencia, Impedimenta, 2021
    libro2 --> 33 Botones, Novela negra, Atlantis, 2022
    libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022
"""
class libreria():
    def __init__(self,nombre,seccion,editorial,año):
        self.nombre = nombre
        self.seccion = seccion
        self.editorial = editorial
        self.año = año

class rosalia(libreria):
    def result(self):
        print(f'el nombre es {self.nombre}')
        print(f'el seccion es {self.seccion}')
        print(f'el editorial es {self.editorial}')
        print(f'el año es {self.año}')


libro1 = rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021)
libro1.result()
libro2 = rosalia("33 Botones", "Novela negra", "Atlantis", 2022)
libro2.result()
libro3 = rosalia("Venganza en Compostela", "Historia", "Universo de letras", 2022)
libro3.result()

# EJERCICIO 2
"""
    2) Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase,
    define una función de nombre misLibros, cuyo resultado sea los datos de los libros:

    libro4 --> Mi primera Novela, Novela, Bruño, 2019
    libro5 --> Gatos, Literatura, Listado, 2018
"""

class milibro(libreria):
    def mislibros(self):
        print(f'el nombre es {self.nombre}')
        print(f'el seccion es {self.seccion}')
        print(f'el editorial es {self.editorial}')
        print(f'el año es {self.año}')

libro4 = milibro("Mi primera Novela", "Novela", "Bruño", 2019)
libro4.mislibros()
libro5 = milibro("Gatos", "Literatura", "Listado", 2018)
libro5.mislibros()

print((libro4.año +libro5.año)/2)