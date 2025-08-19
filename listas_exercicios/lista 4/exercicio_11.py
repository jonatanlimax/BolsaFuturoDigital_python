
#11. Fatorial: Peça um número e calcule seu fatorial usando for.

#pedindo um número ao usuário:
num=int(input("digite um número: "))
fatorial=1
#calculando o fatorial
for n in range(1,num+1):
    fatorial *= n
#exibindo o resultado
print(f"o fatorial de {num} é {fatorial}")