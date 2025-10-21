#Corrigir hierarquia de classes onde subclasses não respeitam a supoerclasse LSP

class Automovel:
    @staticmethod
    def quantidade_rodas(qtd_rodas):
        return qtd_rodas

class Carro(Automovel):
    @staticmethod
    def quantidade_rodas(qtd_rodas):
        return qtd_rodas

