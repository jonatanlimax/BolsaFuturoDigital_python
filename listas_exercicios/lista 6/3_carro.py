#criando a classe carro com atributos modelo e cor
class Carro:
    def __init__(self,modelo,cor):
        self.modelo=modelo
        self.cor=cor

#criando o objeto meu_carro com modelo 'fusca' e cor 'azul'
meu_carro=Carro("Fusca","Azul")
print(f"Inicialmente meu carro {meu_carro.modelo} é de cor {meu_carro.cor}")

#alterando a cor do objeto para 'vermelho'
meu_carro.cor="Vermelho"

#exibindo o novo valor da cor do objeto
print(f"porém o carro modelo {meu_carro.modelo} teve sua cor alterada para {meu_carro.cor}")
