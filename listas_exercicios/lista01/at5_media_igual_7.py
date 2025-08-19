#pedindo a primeira nota do aluno
nota1=float(input("Digite a primeira nota do aluno: "))

#pedindo a segunda nota do aluno
nota2=float(input("digite a segunda nota do aluno: "))

#pedindo a terceira nota do aluno
nota3=float(input("digite a terceira nota do aluno: "))

#calculando a média
media=(nota1+nota2+nota3)/3

#verificando se a média é igual a 7
if media == 7:
    print("a média do aluno é igual a 7")
else:
    print("a média do aluno é diferente de 7")