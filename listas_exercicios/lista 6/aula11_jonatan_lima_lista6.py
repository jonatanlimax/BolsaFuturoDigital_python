#EXERCICIO 1 LISTA 6

#criando a função dobro
def dobro(num):
    return num*2

#criando a função de mostrar
def mostrar(valor):
    print(f"\no dobro do número {numero} é {dobro(valor)}")

#pedindo um número
numero=5
#exibindo o dobro do número através da função mostrar
mostrar(numero)

#-----------------------------------------------------

#EXERCICIO 2 LISTA 6
#criando a classe livro com os atributos titulo e autor
class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor

#criando o metodo exibir dados
    def exibir_dados(self):
        print(f"Titulo: [{self.titulo}], autor [{self.autor}]")

#criando o objeto livro1
livro1=Livro("1984","George Orwell")

#chamando o metodo exibir dados
livro1.exibir_dados()

#-----------------------------------------------
#EXERCICIO 3 LISTA 6
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

#------------------------------------------------------------
#EXERCICIO 4 LISTA 6
#criando função calcular imc
def calcular_imc(peso,altura):
    return peso/(altura**2)

#criando função exibir faixa imc
def exibir_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc <= 24.9:
        return "peso normal"
    elif imc <=29.9:
        return "sobrepeso"
    else:
        return "obesidade"

#atribuindo peso e altura para calcular o imc
peso_altura=calcular_imc(70,1.75)

#chamando a função para exibir o imc
print(exibir_imc(peso_altura))
#-----------------------------------------------
#EXERCICIO 5 LISTA 6
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
#-----------------------------------
#EXERCICIO 6 LISTA 6
#criando a classe pedido com atributos produto e quantidade
class Pedido:
    def __init__(self, produto, quantidade, cliente):
        self.produto=produto
        self.quantidade=quantidade
        self.cliente=cliente

    #criando o metodo de exibir pedido
    def exibir_pedido(self):
        print(f"O cliente {self.cliente.nome} fez o pedido de {self.quantidade} {self.produto}")

#criando a classe cliente com atributo nome
class Cliente:
    def __init__(self, nome):
        self.nome=nome

    #criando o metodo fazer pedido
    def fazer_pedido(self,produto,quantidade):
        return Pedido(produto,quantidade,self) #a palavra self está se referindo ao 'cliente' da classe Pedido

#criando o objeto cliente
cliente1=Cliente("João")

#cliente faz o pedido
pedido1=cliente1.fazer_pedido("Notebook",2)

#chamando o metodo exibir pedido para mostrar o nome do cliente, o produto e quantidade
pedido1.exibir_pedido()
#----------------------------------------------------
#EXERCICIO 7 LISTA 6
#criando a classe ponto
class Ponto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #criando o metodo __str__ que representa o ponto como string
    def __str__(self):
        return f"({self.x},{self.y})"

    #criando o metodo __add__ que permite a soma dos dois pontos
    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

#criando dois objetos p1 e p2
p1 = Ponto(1,2)
p2 = Ponto(3,4)

#atribuindo a soma dos pontos à variável resultado
resultado = p1+p2

#imprimindo o resultado da soma dos pontos
print(resultado)
#---------------------------------------

#EXERCICIO 8 LISTA 6
#criando a classe Turma com atributo aluno sendo lista vazia
class Turma:
    def __init__(self):
        self.alunos=[]

#criando metodo adicionar aluno
    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)

#criando metodo para calcular a media da turma
    def media_turma(self):
        if not self.alunos:
            return 0
        soma = sum(aluno.media() for aluno in self.alunos)
        return soma / len(self.alunos)

#criando a classe Alunos
class Alunos:
    def __init__(self,nome,notas):
        self.nome=nome
        self.notas=notas

    #criando o metodo para calcular media do aluno
    def media(self):
        return sum(self.notas) / len(self.notas)

#criando os alunos
aluno1=Alunos("Carina",[8,7,9])
aluno2=Alunos("Jonatan",[6,5,7])
aluno3=Alunos("Ana",[9,8,9])

#criando a turma
turma1=Turma()
turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)
turma1.adicionar_aluno(aluno3)

#calculando a media da turma
print(f"a média da turma é {turma1.media_turma():.2f}")

#calculando a media de cada aluno
print(f"\na média do {aluno1.nome} é {aluno1.media():.2f}")
print(f"a média do {aluno2.nome} é {aluno2.media():.2f}")
print(f"a média do {aluno3.nome} é {aluno3.media():.2f}")
#---------------------------------------

#EXERCICIO 9 LISTA 6
#criando a classe Motor com atributo potencia
class Motor:
    def __init__(self,potencia):
        self.potencia=potencia
#criando a classe Carro com atributo modelo e motor [o motor é um objeto criado pela classe Motor]
class Carro:
    def __init__(self,modelo,motor):
        self.modelo=modelo
        self.motor=motor
#criando o metodo exibir detalhes que chama o modelo e o objeto motor já com sua potencia
    def exibir_detalhes(self):
        return f"Modelo: {self.modelo}, Motor: {self.motor.potencia} CV"

#criando o motor e carro
motor=Motor(150)
carro=Carro("Ferrari",motor)

#exibindo as informações
print(carro.exibir_detalhes())
#----------------------------

#EXERCICIO 10 (DESAFIO) LISTA 6
#criando a classe Livro com seus atributos titulo, autor e disponibilidade True
class Livro:
    def __init__(self,titulo,autor,disponivel=True):
        self.titulo=titulo
        self.autor=autor
        self.disponivel=disponivel
#criando a classe Biblioteca com atributo livros sendo uma lista vazia
class Biblioteca:
    def __init__(self,livros=None):
        if livros is None:
            livros = []
        self.livros=livros

#criando a classe Usuario com atributo nome
class Usuario:
    def __init__(self,nome):
        self.nome=nome
#criando o metodo para emprestar livros, recebendo o objeto biblioteca e titulo
    def emprestar_livro(self,biblioteca,titulo):
        #valiando se o livro está na biblioteca para exibir mensagem de emprestado ou não
        for livro in biblioteca.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    return f"livro {livro.titulo} emprestado com sucesso"
                else:
                    return f"livro {livro.titulo} indisponível"
#criando os objetos livros
livro1=Livro("a ida","jonatan")
livro2=Livro("a volta", "carina")
livro3=Livro("the chosen", "dalas")

#criando a biblioteca
biblioteca1=Biblioteca([livro1,livro2,livro3])

#criando os usuarios
usuario1=Usuario("ana")
usuario2=Usuario("joão")

#exibindo se o livro foi emprestado
print(f"O {usuario1.emprestar_livro(biblioteca1,livro1.titulo)} para o usuário {usuario1.nome}")
print(f"O {usuario1.emprestar_livro(biblioteca1,livro1.titulo)}, está emprestado ao usuário {usuario1.nome}")
print(f"O {usuario2.emprestar_livro(biblioteca1,livro2.titulo)} para o usuário {usuario2.nome}")
#----------------------------------------------------

#EXERCICIO 3 E 4 AULA 12 - ESTÃO JUNTOS
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
