#criando a função dobro
def dobro(num):
    return num*2

#criando a função de mostrar
def mostrar(valor):
    print(f"\no dobro do número {numero} é {dobro(valor)}")

#pedindo um número
numero=int(input("\ndigite um número: "))

#exibindo o dobro do número através da função mostrar
mostrar(numero)