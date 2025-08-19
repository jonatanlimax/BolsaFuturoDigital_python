#cadastro de produtos

produtos=[]
#pedindo nome de 5 produtos
for n in range(5):
    produto=input("digite o nome de um produto: ")
    #adicionando os produtos na lista
    produtos.append(produto)
#exibindo a lista final com todos os produtos
print(produtos)