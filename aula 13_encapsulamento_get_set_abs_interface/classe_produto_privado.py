# Crie uma classe Produto com atributos privados nome e preco.
# Use getters e setters para garantir que o preço nunca seja negativo.

#criando a classe produto com atributos nome e preço
class Produto:
    def __init__(self,nome,preco):
        self.__nome=nome
        self.__preco=preco

    #metodo getter para o nome
    @property
    def nome(self):
        return self.__nome

    #metodo setter para alterar o nome
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    #metodo getter para o preco
    @property
    def preco(self):
        return self.__preco

    #metodo setter para alterar o preco
    @preco.setter
    def preco(self,novo_preco):
        if novo_preco < 0:
            raise ValueError ("preço inválido, tente novamente")
        self.__preco = novo_preco

#chamdando os metodos
try:
    #definindo o nome e preço do produto
    produto1=Produto("maracuja",5)
    print(f"o produto {produto1.nome} tem o preco R${produto1.preco}")
    #alterando o preco do produto
    produto1.preco=float(input(f"Digite o novo valor do {produto1.nome}: "))
    #alterando o nome do produto
    produto1.nome=input("digite o novo nome: ")
    print(f"o produto teve o nome alterado para {produto1.nome}")

#mensagem de erro ao colocar valor negativo
except ValueError as e:
    print(f"erro {e}")
    print(f"preço não alterado")