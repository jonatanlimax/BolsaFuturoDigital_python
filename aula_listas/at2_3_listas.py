#criando a lista de frutas
frutas=["goiaba", "uva", "morango"]

#criando a lista de docinhos de festa
doces=["brigadeiro","bem casado","beijinho"]

#criando a lista de ingredientes de feijoada
ingredientes_feijoada=["feijão","orelha de porco","rabo de porco","calabresa"]

#salvando as listas em variáveis
f=frutas
d=doces
i=ingredientes_feijoada

#criando uma listona
listona= f + d + i

#chamando o item brigadeiro
print(listona[3])

#adicionando mais 'brigadeiros' a segunda lista de listona
d.append("brigadeiro")
d.append("brigadeiro")

#o que aconteceu com a lista doces? ela recebeu mais dois itens 'brigadeiro' no final da lista
print(doces)

#adicionar 'bebibas' ao final da listona, mas sem criar uma lista
listona.extend(['guaraná','cerveja','vodka'])

print(listona)
