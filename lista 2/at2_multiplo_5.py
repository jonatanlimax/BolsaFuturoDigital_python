#pedindo dois números
num=int(input("digite um número: "))
num2=int(input("digite um número: "))

#verificando se tem algum número multiplo de 5
resultado=num%5 == 0 or num2%5 == 0

print(f"algum número é múltiplo de 5? {resultado}")
