#criando a classe Animal com atributo nome
class Animal:
    def __init__(self,nome):
        self.nome=nome
    #criando o metodo som
    def som(self):
        print("som genérico")
#criando a classe Cachorro que herda Animal
class Cachorro(Animal):
    def som(self):
        print(f"{self.nome} faz: au-au")
#criando a classe Gato que herda Animal
class Gato(Animal):
    def som(self):
        print(f"{self.nome} faz: miau")
#criando a classe Porco que herda Animal
class Porco(Animal):
    def som(self):
        print(f"{self.nome} faz: põe-põe")
#criando a função para exibir o som de todos os animais
def emitir_som(animal):
    animal.som()

#criando a lista de animais
animais=[Cachorro("Luck"),Gato("Makabea"),Porco("Porquinha"),Cachorro("Spaw")]
#exibindo o som de cada animal na lista
for _ in animais:
    emitir_som(_)