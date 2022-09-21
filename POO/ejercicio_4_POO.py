# EJERCICIO 1

"""
    Crea una clase persona. Sus atributos deben ser su nombre y su edad.
    Además crea un método cumpleaños, que aumente en 1 la edad de la persona.
"""
class persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def cumpleaños(self):
        self.edad += 1
    
    def __str__(self):
        print(f'El nombre del cliente es {self.edad}, y la edad es {self.edad}')


# EJERCICIO 2

"""
    Para la clase anterior definir el método str.
    Debe retornar al menos el nombre de la persona.
"""

# EJERCICIO 3

"""
    Extender la clase persona agregando un atributo saldo y un método
     transferencia(self, persona2, monto).
    El saldo representa el dinero que tiene la persona.
    El método transferencia hace que la Persona que llama el
     método le transfiera la cantidad monto al objeto persona2.
    Si no tiene el dinero suficiente no se ejecuta la acción.
"""
class persona():
    def __init__(self,nombre,edad,saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
    
    def cumpleaños(self):
        self.edad += 1
    
    def __str__(self):
        return f'El nombre del cliente es {self.nombre}, la edad es {self.edad} y el importe es {self.saldo}' 

    def transferencia(self,persona2,importe):
        if importe > self.saldo:
            print(f'no se puede hacer la transferencia de {importe} €, por únicamente tener {self.saldo}')
        else:
            persona2.saldo += importe
            persona1.saldo -= importe

persona1 = persona("Juan",30,1000)
persona2 = persona("Luis",20,500)
print(persona1)
print(persona2)
persona1.cumpleaños()
persona2.cumpleaños()
print(persona1)
print(persona2)
persona1.transferencia(persona2,111)
print(persona1)
print(persona2)



