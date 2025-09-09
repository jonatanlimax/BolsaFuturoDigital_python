#criando a classe conta com atributo saldo iniciado em 0
class Conta:
    def __init__(self,saldo=0):
        self.saldo=saldo

    #criando o metodo depositar
    def depositar(self,valor):
        self.saldo += valor

    #criando o metodo sacar
    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    #criando o metodo mostrar informações
    def exibir_saldo(self):
        print(f"o saldo final é {self.saldo}")

#criando um objeto conta
conta1 = Conta()

#chamando o metodo depositar 100
conta1.depositar(100)

#chamando o metodo sacar 30
conta1.sacar(30)

#chamando o metodo exibir saldo
conta1.exibir_saldo()



