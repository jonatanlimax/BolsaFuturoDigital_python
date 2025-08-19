
#8. Soma até negativo: Solicite números até que o usuário digite um número negativo. Mostre a soma dos números positivos digitados.

num = 0
soma = 0

#condição para o loop até digitar negativo
while num >= 0:
    #pedindo para digitar um número
    num = int(input("digite um número positivo para somar ou negativo para parar a soma e mostrar o resultado final: "))
    if num >= 0:
        soma += num
        #exibindo o resultado final
    else:
        print(f"o resultado final é {soma}")
        break