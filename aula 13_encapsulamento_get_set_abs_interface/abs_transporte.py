# 4. (Desafio) Crie um sistema de transporte:
# Classe abstrata Transporte.
# Classes Ônibus, Metrô e Bicicleta que implementem viajar().

#importando o metodo abstrato
from abc import ABC, abstractmethod

#criando a classe abstrata
class Transporte(ABC):
    #criando o metodo abstrato
    @abstractmethod
    def viajar(self,destino,preco,tempo):
        pass
#criando as subclasses para herdar o metodo abstrato
class Onibus(Transporte):
    def __init__(self,destino,preco,tempo):
        self.destino=destino
        self.preco=preco
        self.tempo=tempo

    def viajar(self,destino,preco,tempo):
        return destino, preco, tempo


class Metro(Transporte):
    def __init__(self,destino,preco,tempo):
        self.destino = destino
        self.preco = preco
        self.tempo = tempo

    def viajar(self,destino,preco,tempo):
        return destino, preco, tempo

class Bicicleta(Transporte):
    def __init__(self,destino,preco,tempo):
        self.destino = destino
        self.preco = preco
        self.tempo = tempo

    def viajar(self,destino,preco,tempo):
        return destino, preco, tempo

#chamando Onibus
onibus=Onibus(
    destino=input("Digite o local de destino: "),
    preco=float(input("digite o valor da passagem: ")),
    tempo=float(input("Digite, em horas, o tempo da viagem: "))
)
print(f"a viagem para {onibus.destino} de Ônibus custa R${onibus.preco} e leva {onibus.tempo} horas")

metro=Metro(
    destino=input("Digite o local de destino: "),
    preco=float(input("digite o valor da passagem: ")),
    tempo=float(input("Digite, em horas, o tempo da viagem: "))
)
print(f"a viagem para {metro.destino} de Ônibus custa R${metro.preco} e leva {metro.tempo} horas")

