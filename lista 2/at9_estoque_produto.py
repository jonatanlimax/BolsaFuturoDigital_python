#perguntando a quantiade no estoque
estoque=int(input("qual a quantidade no estoque? "))

#perguntando se é essencial
essencial = input("o produto é essencial? (S/N) ")
resultado = essencial == "s" or  essencial =="S"

#verificando se precisa repor o estoque
if (estoque < 10) or (resultado == True):
    print("Precisa repor o estoque")
else:
    print("não precisa repor o estoque")