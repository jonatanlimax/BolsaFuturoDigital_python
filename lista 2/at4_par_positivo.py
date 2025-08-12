#pedindo um número
num=int(input("digite um número: "))

#verificando se ele é par
par = num%2 == 0

#verificando se é positivo
positivo = num >= 0

#verificando se é par e positivo ao mesmo tempo
if par == True and positivo == True:
    print("par e positivo")
else:
    print("não é par ou positivo")