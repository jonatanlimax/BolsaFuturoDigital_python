#pedindo 3 numeros
num1=float(input("digite um número: "))
num2=float(input("digite um número: "))
num3=float(input("digite um número: "))

#verificando se pelo menos dois são iguais
resultado = (num1 == num2) or (num1 == num3) or (num2 == num3)

print(f"pelo menos dois números são iguais? {resultado}")