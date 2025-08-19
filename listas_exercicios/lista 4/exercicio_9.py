
#9. Adivinhação: Gere um número aleatório de 1 a 20 e peça para o usuário adivinhar, usando while até acertar.

#importando o módulo para gerar números aleatórios
from random import  randint

num = randint(1,20)

#condição para o loop até acertar o número aleatório
while True:
    escolha = int(input("digite um número: "))
    if escolha == num:
        print(f"parabéns! você acertou o número misterioso! ele é {num}")
        break
    else:
        print("não foi dessa vez :( tente novamente")