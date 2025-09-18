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

    #criando o metodo depositar
    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"\nDepósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor inválido!")
#criando o metodo de juros para 5%
    def juros(self):
        aumento = self.saldo*0.05
        print(f"\nO saldo anterior  R${self.saldo:.2f} teve aumento de 5% de juros")
        self.saldo+=aumento
        print(f"seu novo saldo é R${self.saldo:.2f}")

    def transferir(self,valor,conta_destino):
        if self.saldo >= valor > 0:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"transferência de R${valor:.2f} realizada com sucesso  de {self.titular} para {conta_destino.titular}")
            self.extrato()
            conta_destino.extrato()
        else:
            print("Saldo insuficiente")
    #criando o metodo sacar
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"\nSaque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente!")

    #criando metodo para exibir o extrato
    def extrato(self):
        print(f"Conta: {self.conta} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

#criando função adicionar conta
def adicionar_conta():
    global contador_contas
    nome=input("Digite o nome do titular: ").capitalize()
    contador_contas+=1
    conta=ContaBancaria(nome,contador_contas,0)
    contas.append(conta)
    print(f"A conta do titular {nome} foi criada com o número {conta.conta}")

#criando função para exibir as contas
def exibir_contas():
    if not contas:
        print("nenhuma conta cadastrada")
    else:
        for conta in contas:
            conta.extrato()

#função para escolher a conta
def escolher_conta():
    numero = int(input("\nDigite o número da conta: "))
    for conta in contas:
        if conta.conta == numero:
            return conta
    print("Conta não encontrada!")
    return None

#criando função menu de opções
def menu():
    print("############ BANCO NACIONAL ############")
    print("[1] adicionar de conta")
    print("[2] exibir contas")
    print("[3] depositar")
    print("[4] sacar")
    print("[5] exibir extrato")
    print("[6] aplicar 5% de juros")
    print("[7] transferir para outra conta")
    print("[0] sair")
    print("########################################")

#criando menu para opções do menu
def opcoes():
    op = input("digite sua opção: ")
    if op == "1":
        adicionar_conta()
    elif op == "2":
        exibir_contas()
    elif op == "3":
        conta=escolher_conta()
        if conta:
            valor =float(input("digite o valor que deseja depositar: "))
            conta.depositar(valor)
    elif op == "4":
        conta = escolher_conta()
        if conta:
            valor = float(input("digite o valor que deseja sacar: "))
            conta.sacar(valor)
    elif op == "5":
        conta=escolher_conta()
        if conta:
            conta.extrato()
    elif op == "6":
        conta=escolher_conta()
        if conta:
            conta.juros()
    elif op == "7":
        conta_origem = escolher_conta()
        if conta_origem:
            valor=float(input("Digite o valor que deseja transferir: "))
            print("Agora escolha a conta de destino")
            conta_destino = escolher_conta()
            if conta_destino and conta_origem != conta_destino:
                conta_origem.transferir(valor,conta_destino)
            else:
                print("não é possível transferir para a mesma conta")
    elif op =="0":
        print("obrigado por utilizar nosso banco, até mais!")
        return False
    else:
        print("opção inválida, tente novamente")
    return True

#loop para funcionar o menu e as opções
while True:
    menu()
    if not opcoes():
        break


