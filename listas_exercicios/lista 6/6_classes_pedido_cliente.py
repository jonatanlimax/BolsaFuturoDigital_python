#criando a classe pedido com atributos produto e quantidade
class Pedido:
    def __init__(self, produto, quantidade, cliente):
        self.produto=produto
        self.quantidade=quantidade
        self.cliente=cliente

    #criando o método de exibir pedido
    def exibir_pedido(self):
        print(f"O cliente {self.cliente.nome} fez o pedido de {self.quantidade} {self.produto}")

#criando a classe cliente com atributo nome
class Cliente:
    def __init__(self, nome):
        self.nome=nome

    #criando o método fazer pedido
    def fazer_pedido(self,produto,quantidade):
        return Pedido(produto,quantidade,self) #a palavra self está se referindo ao 'cliente' da classe Pedido

#criando o objeto cliente
cliente1=Cliente("João")

#cliente faz o pedido
pedido1=cliente1.fazer_pedido("Notebook",2)

#chamando o método exibir pedido para mostrar o nome do cliente, o produto e quantidade
pedido1.exibir_pedido()