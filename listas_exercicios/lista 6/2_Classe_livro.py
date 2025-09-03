#criando a classe livro com os atributos titulo e autor
class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor

#criando o método exibir dados
    def exibir_dados(self):
        print(f"Titulo: [{self.titulo}], autor [{self.autor}]")

#criando o objeto livro1
livro1=Livro("1984","George Orwell")

#chamando o método exibir dados
livro1.exibir_dados()