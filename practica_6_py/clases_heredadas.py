class ClaseA():
    def __init__(self):
        self.ClaseA = "Esta es la ClaseA"
        print(self.ClaseA)
class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.ClaseB = "Esta es la ClaseB"
        print(self.ClaseB)

class ClaseC(ClaseB):
    def __init__(self):
        super().__init__()
        self.ClaseC = "Esta es la ClaseC"
        print(self.ClaseC)
#Imprimir objeto
Objeto = ClaseC()
print(Objeto)