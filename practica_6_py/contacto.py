class contacto():
    """CLASE"""
    def __init__(self):
        self.nombre = 0
        self.apellido = 0
        self.telefono = 0
        self.direccion = 0

    def SetContacto(self):
        """ATRIBUTOS"""
        print("Ingrese sus datos a continuacion:\n")
        self.nombre = input("Ingrese su Nombre:\n ")
        self.apellido = input("Ingrese sus apellidos:\n ")
        self.telefono = int(input("Ingrese su telefono:\n "))
        self.direccion = input("Ingrese su direccion:\n ")

    def Saludar(self):
        """FUNCION"""
        print("Hola, soy", self.nombre, "", self.apellido, "\nmi numero es", self.telefono,
              "\nmi direccion es", self.direccion)
class ProbarContacto():
    def __init__(self):
        self.Persona1 = contacto()
        self.Persona2 = contacto()

Personas = ProbarContacto()

Personas.Persona1.SetContacto()
Personas.Persona2.SetContacto()
print("Contacto 1\n")
Personas.Persona1.Saludar()
print("Contacto 2\n")
Personas.Persona2.Saludar()