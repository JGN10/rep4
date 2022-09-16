"""
1)** Crea el siguiente programa:\n",
    "* Una clase de nombre Librería\n",
    "* Inicia los siguientes atributos: nombre, sección, editorial y año\n",
    "* Crea una segunda clase con nombre Rosalia que herede la clase librería.\n",
    "* En esta clase Rosalia, crea una función \"result\" cuyo resultado sea los datos de los libros.\n",
    "* declara los Objetos siguientes:\n",
    "    * libro1 --> Oceanarium, Ciencia, Impedimenta, 2021\n",
    "    * libro2 --> 33 Botones, Novela negra, Atlantis, 2022\n",
    "    * libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022"

    """
class libreria():
    def __init__(self,nombre, seccion,editorial,año):
        self.nombre = nombre
        self.seccion = seccion
        self.editorial = editorial
        self.año = año

class rosalia(libreria):
    def result(self):
        print(f'nombre {self.nombre}')
        print(f'seccion {self.seccion}')
        print(f'editorial {self.editorial}')
        print(f'año {self.año}')

libro1 = rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021)
libro2 = rosalia("3 Botones", "Novela negra", "Atlantis", 2022)
libro3 = rosalia("Venganza en Compostela", "Historia", "Universo de letras", 2022)

#libro1.result()
#rosalia.result(libro2)
#libro3.result()
"""
Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase, define una función de nombre misLibros, cuyo resultado sea los datos de los libros:\n",
    "* libro4 --> Mi primera Novela, Novela, Bruño, 2019\n",
    "* libro5 --> Gatos, Literatura, Listado, 2018"
"""

class milibro(rosalia):
    def fun():
        pass

libro4 = milibro("Mi primera Novela", "Novela", "Bruño", 2019)
libro5 = milibro("Gatos", "Literatura", "Listado", 2018)

#rosalia.result(libro4)

#Realiza la media de los años de los libros 4 y 5

def media_edad():
    edad = 2022 - libro4.año
    edad = (edad + (2022 - libro5.año)) /2
    print(f'La edad media de los libros es: {edad}')

#media_edad()

"""
3)** Crea una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos
 para la clase:\n",
    "\n",
    "* Un constructor, donde los datos pueden estar vacíos.\n",
    "* mostrar(): Muestra los datos de la persona.\n",
    "* esMayorDeEdad(): Devuelve un valor indicando si es mayor de edad.
"""

class persona():
    def __init__(self,nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar(self):
        print('estamos en el mostrar de la clase persona')
        print(f'nombre : {self.nombre}')
        print(f'edad {self.edad}')
        print(f'dni {self.dni}')

    def esmayordeedad(self):
        if int(self.edad) >= 18:
            return f"la persona {self.nombre} es mayor de edad"
        else:
            return f"la persona {self.nombre} NO es mayor de edad"
        

persona1 = persona('el nombre',21,None)
persona2 = persona('el nombre de la persona2',10,"000000x")
#persona.mostrar(persona1)
#print(persona.esmayordeedad(persona1))

"""
4 Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y 
cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
 Construye los siguientes métodos para la clase:\n",
    "\n",
    "* Un constructor, donde los datos pueden estar vacíos.\n",
    "* El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.\n",
    "* mostrar(): Muestra los datos de la cuenta.\n",
    "* ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.\n",
    "* retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos si es saldo negativo."
"""
class cuenta():
    def __init__(self,persona,cantidad):
        self.persona = persona
        self.__cantidad = cantidad
    
    def mostrar(self):
        self.persona.mostrar()
        print('volvemos a estar en la clase cuenta')
        print(f'la cantidad {self.__cantidad}')
    
    def ingresar(self,valor):
        if valor >= 0:
            self.__cantidad = self.__cantidad + valor
        else:
            print(' no se puede ingresar nada por se un valor negativo')
        print(f'el valor de cantidad en ingresar es {round(self.__cantidad,2)}')
    
    def retirar(self,valor):
        self.__cantidad = self.__cantidad - valor
        print(f'el valor de cantidad en retirar es {round(self.__cantidad,2)}')



cuenta1 = cuenta(persona1,1000)
#cuenta1.mostrar()
cuenta2 = cuenta(persona2,None)
#cuenta2.mostrar()
#cuenta1.ingresar(-1000)
#cuenta1.ingresar(1111.4)
#cuenta1.retirar(1111.6)
#cuenta1.retirar(1111)
print(cuenta1.persona.nombre)
print(cuenta1.persona.dni)
#print(cuenta1.__cantidad)


"""
 Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
  Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación 
  que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:\n",
    "\n",
    "* Un constructor.\n",
    "* En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., 
    por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad
     pero menor de 25 años y falso en caso contrario.\n",
    "* Además la retirada de dinero sólo se podrá hacer si el titular es válido.\n",
    "* El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.\n",
    "* Piensa los métodos heredados de la clase madre que hay que reescribir."
"""
class CuentaJoven(cuenta):
    def esTitularValido(self):
        if (self.persona.edad >= 18) and (self.persona.edad < 25):
            return True
        else:
           return False
    
    def __init__(self,persona,cantidad,bonificacion):
       ## if self.esTitularValido(persona):
            self.persona = persona
            self.__cantidad = cantidad
            self.bonificacion = bonificacion
        ##else:
        ##    print(f'no se puede crear el objeto')

    def mostrar(self):
        print(f"cuenta joven y bonificacion {self.bonificacion}")

    def ingresar(self,importe):
        if self.esTitularValido():
            self.__cantidad += importe
            print(self.__cantidad)
        else:
            print('no se permite ingresar dinero si tu edad no está entre 18 y 25')

    def retirar(self,importe):
        if self.esTitularValido():
            self.__cantidad -= importe
            print(self.__cantidad)
        else:
            print('no se permite retirar dinero si tu edad no está entre 18 y 25')

cuentajoven1 =  CuentaJoven(persona1,1000,17.2)
print(cuentajoven1.bonificacion)
cuentajoven1.mostrar()
cuentajoven1.ingresar(10000)
cuentajoven1.retirar(1111)


print ('datos cuenta persona 2' )
cuentajoven2 = CuentaJoven(persona2,2000,24.8)
print(cuentajoven2.bonificacion)
cuentajoven2.mostrar()
cuentajoven2.ingresar(10000)
cuentajoven2.retirar(2222)




"""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aea43be0",
   "metadata": {},
   "source": [
    "* Mayor de edad"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8047328",
   "metadata": {},
   "source": [
    "* Menor de edad"
"""