
#2. Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
lista=[]
for n in range(5):
    lista.append(int(input("digite um número:")))
print(min(lista))