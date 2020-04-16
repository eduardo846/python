class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def acelera(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca; ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",
        self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenado: ",self.frena)

    
class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado(self):
        print("Marca; ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",
        self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenado: ",self.frena,"\n",self.hcaballito)

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
    



miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgonera=Furgoneta("Renoult","Kangoo")
miFurgonera.arrancar()
miFurgonera.estado()
print(miFurgonera.carga(True))