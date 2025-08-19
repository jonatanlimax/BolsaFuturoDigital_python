#pedindo o primeiro número
numero1=int(input("digite o primeiro número: "))

#pedindo o segundo número
numero2=int(input("digite o segundo número: "))

#realizando a noma dos dois números
soma=numero1+numero2

# resulado = soma > 20
# print(f"a soma é {soma}. é maior que 20? {resulado}")

#verificando se a soma é maior que 20
if soma > 20:
    print(f"a soma entre {numero1} e {numero2} é igual a {soma}, portanto, é maior que 20")
elif soma == 20:
    print(f"a soma entre {numero1} e {numero2} é igual a {soma}, portanto, é igual 20")
else:
    print(f"a soma entre {numero1} e {numero2} é igual a {soma}, portanto, é menor que 20")