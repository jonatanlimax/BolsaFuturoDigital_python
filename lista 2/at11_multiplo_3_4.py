#pedindo um número
num=int(input("digite um número: "))

#verificando se é multiplo de 3 e 4 ao mesmo tempo
resultado = (num%3==0) and (num%4==0)

print(f"o número é multiplo de 3 e 4 ao mesmo tempo? {resultado}")