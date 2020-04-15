class Coche():
    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4 #encapsular la variable no permite modificarla 
        self.enmarcha=False

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
    def estado(self):
        print("El coche tiene: ",self.__ruedas, "ruedas. Un ancho de ",self.anchoChasis," y un largo de ",
        self.largoChasis)
        


miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-------------A continuacion creamos el segundo objeto-------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

