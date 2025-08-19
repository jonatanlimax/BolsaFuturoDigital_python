#programa escolhe um número (fixo ou aleatório) entre 1 e 10 tenta adivinhar com dicas "maior" ou "menor" usa while até acertar

#importando o randint para gerar números aleatórios
from random import randint
num = randint(1,10)

#estrutura while para o jogo
contador=1
while True:
    escolha = int(input("digite um número entre 1 e 10: "))

    # condição de acerto
    if num == escolha:
        print(f"Parabéns, você acertou! o número misterioso é {num}! \nVocê precisou de apenas {contador} chances para acertar o número misterioso!")
        break

    #condição com dica menor
    elif num > escolha:
        print("não foi dessa vez :( mas o número que você digitou é menor que o número misterioso, tente novamente")
        contador += 1
    # condição com dica maior
    else:
        print("não foi dessa vez :( mas o número que você digitou é maior que o número misterioso, tente novamente")
        contador += 1