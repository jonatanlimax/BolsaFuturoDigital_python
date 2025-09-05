#criando a lista de contas
contas = []

#criando contador de contas
contador_contas = 0

#criando a classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular="", conta=0, saldo=0):
        self.titular=titular
        self.conta=conta
        self.saldo=saldo

    #criando metodo adicionar conta
    def adicionar_conta(self):
        self.titular = input("Digite o nome do titular: ").capitalize()
        self.conta = contador_contas
        self.saldo = 0
        contas.append({
            "conta": self.conta,
            "titular": self.titular,
            "saldo R$": self.saldo
        })

    #criando metodo para exibir contas
    def exibir_contas(self):
        if len(contas) == 0:
            print("Nenhuma conta cadastrada")
        else:
            for conta in contas:
                print(conta)

    #criando o metodo depositar
    def depositar(self):
        deposito = float(input("Digite o valor que deseja depositar: R$"))
        if deposito <= 0:
            print("Valor incorreto, tente novamente.")
        else:
            self.saldo += deposito
            print(f"o depósito no valor de R${deposito} foi efetuado com sucesso!")

    #criando metodo menu de opções
def menu():
    print("[1] cadastro de conta")
    print("[2] exibir contas")
    print("[3] depositar")
    print("[4] sacar")
    print("[5] exibir extrato")
    print("[0] sair")

def opcoes():
    op=int(input(("Escolha uma das opções do menu acima: ")))
    if op == 1:
        cliente.adicionar_conta()

while True:
    contador_contas += 1
    cliente=ContaBancaria()
    menu()
    opcoes()

    # cliente1 = ContaBancaria()
    # cliente1.menu()
    # cliente1.adicionar_conta(contador_contas)
    # cliente1.exibir_contas()
