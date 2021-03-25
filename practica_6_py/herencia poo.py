class Persona ():
    """CLASE QUE REPRESENTA PERSONA"""
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
    def estado(self):
        print("Nombre: ", self.nombre, "\nApellido: ", self.apellido, "\nCedula: ", self.cedula, "\nEdad: ", self.edad)

Persona1 = Persona("Jose", "Martinez", "402-475873-2", "25")

Persona1.estado()
print("\nProfesor")
class Profesor(Persona):
    """HERENCIA DE CLASE"""
    sueldo=""
    def sueld(self):
        self.sueldo = "50000"
    def estado(self):
        print("Nombre: ", self.nombre, "\nApellido: ", self.apellido, "\nCedula: ", self.cedula, "\nEdad: ", self.edad,
              "\nSueldo:" , self.sueldo)
Persona2 = Profesor("Manuel", "Guzman", "127-64736473-5", "37")

Persona2.sueld()
Persona2.estado()