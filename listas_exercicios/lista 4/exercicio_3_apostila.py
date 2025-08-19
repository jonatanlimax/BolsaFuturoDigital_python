
# #3. Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver ordenada de forma crescente ou False
# caso contrário.

lista=[]

for n in range(5):
    lista.append(int(input("digite um número: ")))
print(lista)
lista_ordenada=[lista.sort()]

print(lista==lista_ordenada)