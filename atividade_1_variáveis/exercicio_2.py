# 2. Opera¸c˜oes com Strings
# Dada a string "Python ´e incr´ıvel!", fa¸ca o seguinte:
# • Conte quantos caracteres ela possui (incluindo espa¸cos)
# • Converta toda a string para mai´usculas
# • Substitua a palavra ”incr´ıvel”por ”poderoso”
# Sa´ıda Esperada:
# 18
# PYTHON I N C R V E L !
# Python poderoso !

#---------------------------#

#atribuindo a string à variável 'a'
a="Python é incrível!"

#realizando a contagem dos caracteres incluindo espaços
qtd=len(a)

#imprimindo a quantidade de caracteres
print(qtd)

#convertendo para maiúsculo
maior=a.upper()

#imprimindo a string em maiusculo
print(maior)

#substituindo a palavra 'incrível' por 'poderoso'
subst=a.replace("incrível","poderoso")

#imprimindo
print(subst)