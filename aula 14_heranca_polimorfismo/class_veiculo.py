    #criando a classe 'pai' Veiculo com atributos marca e modelo
    class Veiculo:
        def __init__(self, marca, modelo,cor):
            self.marca=marca
            self.modelo=modelo
            self.cor=cor
    #criando o metodo ligar
        def ligar(self):
            return "o veículo está ligado"

    #criando a classe Carro que herda Veiculo
    class Carro(Veiculo):
        #metodo ligar com mensagem personalizada para carro
        def ligar(self):
            return "o carro ligou"
    #criando a classe Moto que herda Veiculo
    class Moto(Veiculo):
        #criando o metodo ligar com mensagem personalizada para moto
        def ligar(self):
            return "a moto ligou"

    #criando o objeto carro1 e imprimindo a mensagem de ligar
    carro1=Carro("fiat","uno","rosa")
    print(carro1.ligar())

    #criando o objeto moto1 e imprimindo a mensagem de ligar
    moto1=Moto("honda","cg","preta")
    print((moto1.ligar()))
