class ContaBanc:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo

    def depositar(self):
        deposito = float(input("\nDigite o valor que deseja depositar R$: "))
        if deposito > 0:
            self.saldo+=deposito
            print(f"\nfoi realizado um depósito de R${deposito:.2f} e o saldo de {self.titular} é R${self.saldo:.2f}")
        else:
            print("O valor de depósito não pode ser menor ou igual a zero ")

    def sacar(self):
        saque = float(input("\nDigite o valor que deseja sacar R$: "))
        if saque <= self.saldo:
            self.saldo-=saque
            print(f"\nfoi realizado um saque de R${saque:.2f} e saldo de {self.titular} é R${self.saldo:.2f}")
        else:
            print(f"\n{self.titular} não tem saldo suficiente")

cliente1=ContaBanc(
    titular=input("\nDigite o nome do titular: "),
    saldo=float(input("\nDigite o valor do saldo R$: "))
)

cliente1.depositar()
cliente1.sacar()