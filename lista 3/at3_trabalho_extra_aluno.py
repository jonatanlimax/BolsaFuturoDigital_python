#pedindo a nota do aluno
nota=float(input("digite a nota do aluno: "))

#perguntando se o aluno fez o trabalho extra
trabalho=input("você fez o trabalho extra? (S/N) ")
resultado = trabalho == "s" or trabalho == "S"

#verificando se o aluno foi aprovado
if (nota >= 7) or resultado == True:
    print("aprovado")
else:
    print("reprovado")