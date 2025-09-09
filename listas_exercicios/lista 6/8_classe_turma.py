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

