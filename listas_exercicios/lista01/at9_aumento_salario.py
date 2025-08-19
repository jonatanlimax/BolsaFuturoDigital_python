#pedindo o valor do salario do usuario
salario = float(input("digite o seu salario: "))

#calculando o aumento do funcionario considerando 15%
aumento=salario * 0.15

#calculando o novo salario do funcionario
salario_novo= salario + aumento

#exibindo o novo salario
print(f"o antigo salario do funcionario é R${salario}, mas com aumento de 15% seu novo salario passa a ser R${salario_novo}")