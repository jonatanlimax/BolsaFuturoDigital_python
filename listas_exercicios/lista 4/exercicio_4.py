
#4.Soma de números: Peça 5 números ao usuário e mostre a soma total.
soma=0

for n in range(5):
    num = int(input("digite um número: "))
    soma += num
print(f"a soma dos números digitados foi: {soma}")