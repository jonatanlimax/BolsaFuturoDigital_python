#pedindo o primeiro número ao usuario
numero1=float(input("digite o primeiro número: "))

#pedindo o segundo número ao usuário
numero2=float(input("digite o segundo número: "))

#verificando se são iguais
if numero1 == numero2:
    print("os números digitados pelo usuário são iguais")
elif numero1 > numero2:
    print(f"o número {numero1} é maior que o número {numero2}")
else:
    print(f"o número {numero2} é maior que o número {numero1}")

#sem usar if else
resultado = numero1==numero2
print(f"os números são iguais? {resultado} ")