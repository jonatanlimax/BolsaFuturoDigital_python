# 2. Crie uma classe abstrata Funcionario com metodo abstrato
# calcular_salario().
# Crie Gerente e Vendedor que implementem de formas diferentes.

#importando o metodo abstrato
from abc import ABC, abstractmethod

#criando a classe abstrata
class Funcionario(ABC):
    #criando o metodo abstrato com seus atributos
    @abstractmethod
    def calcular_salario(self, base, valor_variavel):
        pass
#criando a subclasse gerente que herda a classe abstrata
class Gerente(Funcionario):
    def __init__(self, base, meta):
        self.base=base
        self.meta=meta
    def calcular_salario(self,base,meta):
        salario = base + 0.3*meta
        return salario
#criando a subclasse venderdor que herda a classe abstrata
class Vendedor(Funcionario):
    def __init__(self, base, vendas):
        self.base=base
        self.vendas=vendas
    def calcular_salario(self,base,vendas):
        salario = base + 0.05*vendas
        return salario

#chamando as classes abstratas
gerente1=Gerente(3500,1000)
print(f"O gerente tem o salário base de R${gerente1.base} e a meta a ser batida é R${gerente1.meta}, dando bonus de 30% sobre a meta. O novo salário do gerente é R${gerente1.calcular_salario(gerente1.base,gerente1.meta):.2f}")

vendedor1=Vendedor(1500,300)
print(f"O vendedor tem salário base R${vendedor1.base} e ele recebe 5% das vendas, que nesse mês deu R${vendedor1.vendas}. O novo salário do vendedor é R${vendedor1.calcular_salario(vendedor1.base,vendedor1.vendas):.2f}")
