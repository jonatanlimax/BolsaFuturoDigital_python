
#7. Contar positivos e negativos: Peça 6 números e conte quantos são positivos, negativos ou zero.

#pedindo números ao usuário
cont_positivo=0
cont_negativo=0
cont_zero=0

for n in range(6):
    num = int(input("digite um número: "))
    if num > 0:
        cont_positivo += 1
    elif num < 0:
        cont_negativo += 1
    else:
        cont_zero += 1

#imprimindo o resultado
print(f"o usuário digitou {cont_zero} números 0,\n{cont_negativo} números negativos e\n{cont_positivo} números positivos")