# EJERCICIO 1
"""
    Crea una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    mostrar(): Muestra los datos de la persona.
    esMayorDeEdad(): Devuelve un valor indicando si es mayor de edad.
"""
class persona():
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar(self):
        return(f'los datos de la persona son nombre: {self.nombre}, edad: {self.edad}, dni: {self.dni}')

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

persona1=persona('Juan',10,'00000x')
persona2=persona('Ana',23,'99999t')
print(persona1.mostrar())
print(persona1.esMayorDeEdad())

# EJERCICIO 2
"""
    Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) 
    y cantidad (puede tener decimales).
    Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    mostrar(): Muestra los datos de la cuenta.
    ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos si es saldo negativo.
"""
class cuenta():
    def __init__(self,persona,cantidad):
        self.persona  = persona
        self.__cantidad = cantidad

    def mostrar(self):
        return f"los datos de la cuenta son: {self.persona.mostrar()}, la cantidad es: {self.__cantidad} "

    def ingresar(self,cantidad):
        if cantidad < 0:
            print('No se puede ingresar en la cuenta un valor negativo')
        else:
            self.__cantidad += cantidad
    
    def retirar(self,cantidad):
        self.__cantidad -= cantidad
        if self.__cantidad < 0:
            print(f'La cantidad de la cuenta está en números rojos: {self.__cantidad}')
      
cuenta1 = cuenta(persona1,1000)
cuenta2 = cuenta(persona2,2000)
print(cuenta1.mostrar())
print(cuenta2.mostrar())
cuenta1.ingresar(111)            
cuenta1.ingresar(-111) 
cuenta2.retirar(1000)
cuenta2.retirar(1500)
print(cuenta1.mostrar())
print(cuenta2.mostrar())

    

# 1) Ingresar en positivo

# 2) Ingresar negativo

# 3) Retirar dinero

# 4) Retirar dinero en número rojos


# EJERCICIO 3

"""
    Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
    Cuando se crea esta nueva clase, además del titular y la cantidad se
    debe guardar una bonificación que estará expresada en tanto por ciento.
    Construye los siguientes métodos para la clase:

    Un constructor.
    En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad,
    por lo tanto hay que crear un método esTitularValido() que devuelve verdadero
    si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

    Además la retirada de dinero sólo se podrá hacer si el titular es válido.

    El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    Piensa los métodos heredados de la clase madre que hay que reescribir.
"""
class cuentajoven(cuenta):
    def valida_edad(self,edad):
        if (edad >= 18) and (edad < 25):
            return False
        else:
            return True

    
    def __init__(self,persona,cantidad,bonificacion):
        if (persona.edad >= 18) and (persona.edad < 25):
            super().__init__(persona,cantidad)
            self.bonificacion=bonificacion
        else:
            print ('No se puede crear la cuenta por no se un cliente válido')

    def esTitularValido(self):
        return self.valida_edad(self.persona.edad)
    
    def retirar(self,importe):
        if self.esTitularValido():
            super().retirar(1000)
        else:
            print('Titular no válido para retirar')

    def ingresar(self,importe):
        super().ingresar(2000)

    def mostrar(self):
        return f" cuenta Joven sus datos son: {super().mostrar()}, y la bonificación es {self.bonificacion}  "
print("ejercicio 333333333333333333333333333333333333")
cuentajoven1=cuentajoven(persona1,3000,17.5)
cuentajoven2=cuentajoven(persona2,5000,12.5)
print(cuentajoven2)
print(cuentajoven1)
print(f'la bonificacion de cuenta1 {cuentajoven1.bonificacion}')
print(cuentajoven2.valida_edad(10))
print(cuentajoven1.mostrar())
print(cuentajoven2.mostrar())
print(cuentajoven2.esTitularValido())
#cuentajoven1.retirar(2000)
cuentajoven2.retirar(2000)
#print(cuentajoven1.mostrar())
print(cuentajoven2.mostrar())

#cuentajoven1.ingresar(2000)
cuentajoven2.ingresar(2000)
#print(cuentajoven1.mostrar())
print(cuentajoven2.mostrar())




    


# 1) Mayor de edad

# 2) Menor de edad

