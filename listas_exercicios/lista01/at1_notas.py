#pedindo a primeira nota do aluno
nota1=float(input("Digite a primeira nota do aluno: "))

#pedindo a segunda nota do aluno
nota2=float(input("digite a segunda nota do aluno: "))

#pedindo a terceira nota do aluno
nota3=float(input("digite a terceira nota do aluno: "))

#calculando a média
media=(nota1+nota2+nota3)/3

#imprimindo as notas do aluno e respectiva média
print(f"o aluno teve a primeira nota {nota1}, segunda nota {nota2} e terceira nota {nota3}, assim, sua média foi calculada em {media:.2f}")