# EJERCICIO 1

"""
    Crearemos una clase llamada NumeroComplejo.
    Este tipo tiene un atributo x para la coordenada en x e y para la coordenada en y.
    Representa un número complejo de la forma (x, y).
"""
class NumeroComplejo():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Los valores del número complejo son x: {self.x}, son y {self.y} ')

    def __str__(self):
        print(f'Los valores del número complejo son x: {self.x}, son y {self.y} ')
        return ""

    def compara(self,numero):
        if (self.x == numero.x) and (self.y == numero.y):
            return "Iguales"
        else:
            return "diferentes"

    def suma(self,numero):
        return NumeroComplejo(self.x+numero.x,self.y+numero.y)

numero1 = NumeroComplejo(11,12)
numero2 = NumeroComplejo(21,92)
numero1.imprimir()
print(numero1)
print(numero1.compara(numero2))
numero3 = numero1.suma(numero2)
print(numero3)

# se pueden definir operaciones como la suma, resta, multiplicación, etc 
# las funciones son __add__, __sub__, __mul__ etc... hay mchas más


# EJERCICIO 2

"""
    Ahora defina dentro de la clase NumeroComplejo un función imprimir
    donde muestre los valores de x e y.
"""

# EJERCICIO 3

"""
    Define la función str para la clase NumeroComplejo
    para poder imprimir usando la función print.
"""
# EJERCICIO 4

"""
    Define una función que compara dos números complejos,
    ya que si dos objetos distintos tienen sus atributos iguales,y
    sino NO se consideran iguales.
"""
    


# EJERCICIO 5

"""
    Realiza un método que sume dos numeros complejos sin modificiar los objetos originales,
    ya que se retorna un nuevo numero NumeroComplejo.
"""

    

