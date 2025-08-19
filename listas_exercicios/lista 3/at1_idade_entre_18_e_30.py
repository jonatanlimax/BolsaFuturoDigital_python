#pedindo a idade
idade=int(input("Digite sua idade: "))

#verificando se a idade está entre 18 e 30 anos
resultado = (idade >= 18) and (idade <= 30)

print(f"a idade da pessoa está entre 18 e 30 anos? {resultado}")