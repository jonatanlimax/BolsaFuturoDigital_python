#soma de números pares

#pedindo 5 números ao usuário
soma=0
for n in range(5):
    num=(int(input("digite um número: ")))
#somando os números pares
    if num % 2 == 0:
        soma += num
#exibindo o resultado final
print(f"a soma dos números pares é igual a {soma}")