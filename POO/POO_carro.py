class Carro:
    def __init__(self,modelo,ano):
        self.modelo=modelo
        self.ano=ano

    def mostrar(self):
        print(f"o carro modelo {self.modelo} e seu ano é {self.ano}")

carro1=Carro(
    modelo = input("digite o modelo: "),
    ano=input("digite o ano: ")
)

carro1.mostrar()
