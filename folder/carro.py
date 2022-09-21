class Carro:

    def __init__(self, cor, ligado=False, velocidade=0, espelhamento=False, pelicula=False):
        self.cor = cor
        self.ligado = ligado
        self.velocidade = velocidade
        self.espelhamento = espelhamento
        self.pelicula = pelicula

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            self.ligado = False

    def acelerar(self, aceleracao):
        if self.ligado:
            self.velocidade += aceleracao

    def modificar(self, nova_cor, novo_espelhamento, nova_pelicula):
        self.cor = nova_cor
        self.espelhamento = novo_espelhamento
        self.pelicula = nova_pelicula
