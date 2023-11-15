class Arma:
    def __init__(self, tipo, velocidadDisparo, bala, cargador, complementos, daño):
        self.tipo = tipo
        self.velocidadDisparo = velocidadDisparo
        self.bala = bala
        self.cargador = cargador
        self.complementos = complementos
        self.daño = daño

class Pistola(Arma):
    def __init__(self):
        pass
    
    def Glock17(self):
        self.tipo = "Glock 17"
        self.velocidadDisparo = "Monotiro"
        self.bala = "19 mm"
        self.cargador = "15 balas"
        self.complementos = "Silenciador"
        self.daño = 9