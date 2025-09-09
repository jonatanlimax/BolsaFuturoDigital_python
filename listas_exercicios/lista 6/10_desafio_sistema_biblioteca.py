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