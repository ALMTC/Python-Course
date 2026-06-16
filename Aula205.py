class Camera:
    def __init__(self, modelo, gravando=False):
        self.modelo = modelo
        self.gravando = gravando
    
    def gravar(self):
        if self.gravando:
            print(f"{self.modelo} já está gravando")
            return
        
        self.gravando = True
        print(f"{self.modelo} começou a gravar")

    def fotografar(self):
        if self.gravando:
            print(f"{self.modelo} não pode fotografar enquanto grava")
            return
        print(f"{self.modelo} tirou a foto")

    def parar_de_gravar(self):
        if self.gravando:
            self.gravando = False
            print(f"{self.modelo} parou de gravar")
            return
        print(f"{self.modelo} não está gravando")
    
c1 = Camera("Cannon")
c2 = Camera("Sony")

c1.gravar()
c1.fotografar()
c1.parar_de_gravar()
c2.fotografar()