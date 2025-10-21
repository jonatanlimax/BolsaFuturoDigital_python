#refatorar uma classe que mistura calculos e prints; seperar responsabilidades em classes dinstintas


#SEM REFATORAR
# class Media:
#     def __init__(self,nota1=0,nota2=0,media=0):
#         self.nota1 = nota1
#         self.nota2 = nota2
#         self.media = media
#
#     def calcular_media(self):
#         self.nota1=float(input("digite a primeira nota: "))
#         self.nota2=float(input("digite a segunda nota: "))
#         self.media=(self.nota1+self.nota2)/2
#
#     def mostrar_media(self):
#         print(f'a média do aluno é {self.media:.2f}')
#
# aluno=Media()
# aluno.calcular_media()
# aluno.mostrar_media()

#REFATORANDO

class PedirNotas:
    @staticmethod
    def pedir_notas():
        try:
            nota1 = float(input("digite a primeira nota: "))
            nota2 = float(input("digite a segunda nota: "))
            return nota1,nota2
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números.")
            return None, None  # Retorna None para indicar falha

class CalcularMedia:
    """
        Responsabilidade Única: Realizar o cálculo da média.
        Recebe os dados brutos e retorna o resultado processado.
        """
    @staticmethod
    def calcular_media(nota1,nota2):
        if nota1 is not None and nota2 is not None:
            return (nota1+nota2)/2
        return None

class ExibirMedia:
    """
        Responsabilidade Única: Exibir o resultado final ao usuário.
        Recebe o resultado processado e formata a saída.
        """
    @staticmethod
    def exibir_media(media):
        if media is not None:
            print(f"a média do aluno é {media:.2f}")
        else:
            print("não foi possível calcular a média, dados inválidos")

aluno = PedirNotas()
nota_a,nota_b = aluno.pedir_notas()
media_ok=CalcularMedia.calcular_media(nota_a,nota_b)
ExibirMedia.exibir_media(media_ok)

