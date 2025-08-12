#pedindo a idade
idade=int(input("digite sua idade: "))

#perguntando se tem autorização dos pais
autorizacao=input("voce tem autorização dos seus pais? (S/N) ")
resultado = autorizacao == "s" or autorizacao == "S"

#verificando se pode entrar
if (idade >= 18) or (resultado == True):
    print("entrada permitida")
else:
    print("entrada proibida")