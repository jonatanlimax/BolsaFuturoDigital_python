#pedindo a idade
idade=int(input("Digite sua idade: "))

#perguntando se tem carteira de motorista
motorista=input("você tem carteira de motorista? (S/N) ")
resultado = motorista == "s" or motorista == "S"

#verificando se pode dirigir
if (idade >= 18) and (resultado == True):
    print("Você pode dirigir")
else:
    print("você não pode dirigir")