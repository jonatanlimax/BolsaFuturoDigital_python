#pedindo um número ao usuario
numero=int(input("digite um número: "))

#calculando o resto da divisão por 3
resto=numero%3

#verificando se o resto da divisão é igual a 1
if resto == 1:
    print("o resto da divisão é igual a 1")
else:
    print("o resto da divisão é diferente de 1")