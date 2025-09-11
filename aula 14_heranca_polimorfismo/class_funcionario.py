#importando o modulo abstrato
from abc import ABC, abstractmethod
#criando a classe abstrata Funcionario
class Funcionario(ABC):
    #definindo o metodo abstrato calcular_salario com atributo base e salario_variado
    @abstractmethod
    def calcular_salario(self,base,salario_variado):
        pass
#criando a classe Gerente que está herdando Funcionario e seu metodo abstrato
class Gerente(Funcionario):
    #aplicando o polimorfismo para calcular o salario do gerente
    def calcular_salario(self,base,meta):
        salario=base+0.3*meta
        return salario

#criando a classe Vendedor que herda o metodo abstrato de Funcionario
class Vendedor(Funcionario):
    #aplicando o polimorfismo
    def calcular_salario(self,base,comissao):
        salario = base + 0.05*comissao
        return salario

#criando o objeto gerente1 instanciado à classe Gerente
gerente1=Gerente()
#imprimindo o salário do gerente1
print(gerente1.calcular_salario(3000,5000))

#criando o objeto vendedor1 instanciado à classe Vendedor
vendedor1=Vendedor()
#imprimindo o salário do vendedor
print(vendedor1.calcular_salario(1512,500))