# 5. Tuplas e Conjuntos
# Dada a tupla cores = ("vermelho", "verde", "azul", "verde"):
# • Converta-a em um conjunto para remover duplicatas
# • Adicione a cor "amarelo" ao conjunto
# Sa´ıda Esperada:
# {’vermelho ’, ’verde ’, ’azul ’, ’amarelo ’}

cores = ("vermelho", "verde", "azul", "verde")

#convertendo de tuplas para conjunto, removendo a duplicada 'verde'
convert= set(cores)

#imprimindo o resultado
print(convert)

#adicionando 'amarelo'
convert.add("amarelo")

#imprimindo o resultado
print(convert)


