#criando a classe carro com atributos modelo e cor
class Carro:
    def __init__(self,modelo,cor):
        self.modelo=modelo
        self.cor=cor

#criando o objeto meu_carro com modelo 'fusca' e cor 'azul'
meu_carro=Carro("Fusca","Azul")

#alterando a cor do objeto para 'vermelho'
meu_carro.cor="Vermelho"

#exibindo o novo valor da cor do objeto
print(f"o carro modelo {meu_carro.modelo} e sua cor é {meu_carro.cor}")
