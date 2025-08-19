# 8. Manipula¸c˜ao de Strings
# Dada a string "programa¸c~ao":
# • Inverta a string
# • Verifique se a string original ´e igual `a string invertida
# Sa´ıda Esperada:
# o a m a r g o r p
# False

#-----------------#

a = "programação"

#invertendo a string
invertido = a[::-1]

#imprimindo resultado
print(invertido)

#verificando se as strings são iguais
print(a==invertido)