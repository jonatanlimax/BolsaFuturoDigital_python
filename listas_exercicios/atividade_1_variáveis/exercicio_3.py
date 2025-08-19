# 3. Listas e Indexa¸c˜ao
# Dada a lista numeros = [10, 20, 30, 40, 50], fa¸ca:
# • Acesse e imprima o terceiro elemento
# • Adicione o n´umero 60 no final da lista
# • Remova o n´umero 20 da lista
# Lista Final Esperada:
# [10 , 30 , 40 , 50 , 60]

#-------------------#

numeros = [10, 20, 30, 40, 50]

#imprimindo o terceiro elemento
print(numeros[2])

#adicionando o número 60 no final da lista
numeros.append(60)

#imprimindo a lista com a adição do 60
print(numeros)

#deletando o número 20
del numeros[1]

#imprimindo o resultado
print(numeros)