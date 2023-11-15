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

    def disparar(self, sonido, tiempo):
        self.sonido = sonido
        self.tiempo = tiempo
        print(sonido)
        print(tiempo)

    def Glock17(self):
        self.tipo = "Glock 17"
        self.velocidadDisparo = "Monotiro"
        self.bala = "19 mm"
        self.cargador = "15 balas"
        self.complementos = "Silenciador"
        self.daño = 9

pistola = Pistola()
for i in range(1,4):
    pistola.disparar('BANG', i)