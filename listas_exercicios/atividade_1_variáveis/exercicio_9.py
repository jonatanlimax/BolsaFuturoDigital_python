# 9. Listas Aninhadas
# Dada a lista matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
# • Acesse e imprima o n´umero 5
# • Substitua o n´umero 8 por 10
# Lista Modificada Esperada:
# [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 10 , 9]]

#--------------#
lista=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#acessando e imprimindo o número 4
print(lista[1][1])

#alterando o número 8 por 10
lista[2][1]=10
print(lista)