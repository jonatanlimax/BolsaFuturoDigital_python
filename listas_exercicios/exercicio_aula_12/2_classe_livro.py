#criando a classe livro
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    #criando o metodo detalhes
    def detalhes(self):
        print(f"O livro [{self.titulo}] foi escrito pelo autor [{self.autor}] e possui [{self.paginas}] páginas")

#criando o objeto livro
livro1 = Livro(
    titulo=input("Digite o título do livro: "),
    autor=input("Digite o autor do livro: "),
    paginas=int(input("Digite a quantidade de páginas do livro: "))
)

#chamando o metodo detalhes
livro1.detalhes()