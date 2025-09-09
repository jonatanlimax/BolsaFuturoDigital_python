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