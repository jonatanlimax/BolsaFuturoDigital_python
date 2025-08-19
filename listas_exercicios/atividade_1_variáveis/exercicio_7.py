# 7. Verifica¸c˜ao de Tipos
# Dada a lista dados = [42, 3.14, "Python", True, [1, 2]], percorra cada elemento
# e imprima seu tipo.
# Sa´ıda Esperada:
# <class ’int ’>
# <class ’float ’>
# <class ’str ’>
# <class ’bool ’>
# <class ’list ’>

#----------------#

lista=[42, 3.14, "Python", True, [1, 2]]

#percorrendo cada elemento e imprimindo seu tipo
for lista in lista:
    print(type(lista))