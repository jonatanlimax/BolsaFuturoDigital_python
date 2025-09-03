#criando a classe carro
class Carro:
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    #criando o metodo acelerar
    def acelerar(self):
        acelerar = int(input("Digite o valor da aceleração: "))
        self.velocidade += acelerar
        print(f"A velocidade do {self.marca} {self.modelo} após acelerar {acelerar}Km/h é {self.velocidade}Km/h")

    #criando o metodo frear
    def frear(self):
        frear = int(input("Digite o valor da frenagem: "))
        if frear > self.velocidade:
            print(f"A velocidade de frenagem é maior que a velocidade do carro")
        else:
            self.velocidade -= frear
            print(f"A velocidade do {self.marca} {self.modelo} após frear {frear}Km/h é {self.velocidade}Km/h")

    #criando o metodo parar o carro
    def parar(self):
        self.velocidade = 0
        print(f"O {self.marca} {self.modelo} parou com segurança, parabéns, motorista!")

#criando o objeto carro com marca e modelo, a velocidade está definida como 0
carro1 = Carro(
    marca = input("Digite a marca do carro: "),
    modelo = input("Digite o modelo do carro: ")
)

#criando a função para escolher se o carro acelera ou freia
def opcao():
    while True:
        op = input("digite 1 para acelerar e 2 para frear ou 0 para parar o carro: ")
        if op == "1":
            carro1.acelerar()
        elif op == "2":
            carro1.frear()
        elif op == "0":
            carro1.parar()
            break
        else:
            print("opção incorreta, tente novamente")

#chamando a função de escolha
opcao()


