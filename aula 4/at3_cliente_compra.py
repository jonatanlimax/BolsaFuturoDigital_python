#pedindo o nome do cliente
nome=input("qual o nome do cliente? ")
print("")

#pedindo o valor da compra
compra=float(input("digite o valor da compra: "))
print("")

#perguntando o nível do cliente
menu='''(1) - comum
(2) - vip 
(3) - premium
 '''
print(menu)
print("")
nivel = input("digite o número correspondente ao nível do cliente: ")
print("")
#aplicando desconto de 0% para comum, 10% para vip e 20% para premium
if nivel == "1":
    desconto = 0
    print(f"o cliente {nome} é nível comum e não tem desconto, valor da compra R${compra}")
elif nivel == "2":
    desconto = compra*0.9
    print(f"o cliente {nome} é nível vip e tem desconto de 10%, valor da compra R${desconto}")
elif nivel == "3":
    desconto = compra * 0.8
    print(f"o cliente {nome} é nível premium e tem desconto de 20%, valor da compra R${desconto}")
else:
    print("nível errado, tente novamente")