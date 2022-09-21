from carro import Carro

c1 = Carro('Amarelo')
print(vars(c1))
c1.modificar('Preto', True, True)
c1.ligar()
c1.acelerar(50)
print(vars(c1))
