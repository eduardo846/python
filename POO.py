class Coche():
    #propiedades de un objeto
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    #comportamiento de un objeto
    def arrancar(self):
        self.enmarcha=True
    
    def estado(self):
        if(self.enmarcha):
            return("EL coche esta en marcha")
        else:
            return("EL coche esta parado ")


miCoche=Coche() #instancia de una clase
print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene: ",miCoche.ruedas," ruedas")
miCoche.arrancar()
print(miCoche.estado())

