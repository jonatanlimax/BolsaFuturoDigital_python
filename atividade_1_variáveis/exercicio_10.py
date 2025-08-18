# 10. Desafio Final
# Crie um dicion´ario estoque com:
# • "ma¸c~a": 10
# • "banana": 5
# • "laranja": 8
# Fa¸ca o seguinte:
# • Adicione "pera" com quantidade 12
# • Remova "banana"
# • Imprima apenas os nomes dos itens (chaves)
# Sa´ıda Esperada:
# dict_keys ([ ’ m a ’, ’laranja ’, ’pera ’])
# from docutils.utils.smartquotes import educateQuotes

#-------------#

estoque={"maçã":10,"banana":5,"laranja":8}

#adicionando 'pera' = 12
estoque["pera"]=12

#deletando 'banana'
del(estoque["banana"])

#imprimindo as alterações
print(estoque)

#imprimindo apenas os nomes dos itens
print(estoque.keys())