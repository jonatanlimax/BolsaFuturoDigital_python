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