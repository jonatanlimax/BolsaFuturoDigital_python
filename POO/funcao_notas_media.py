def media(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3

def mostrar(valor):
    print(f"\na média é {valor:.2f}")

def pedir_nota():
    nota1=float(input("digite a primeira nota: "))
    nota2=float(input("\ndigite a segunda nota: "))
    nota3=float(input("\ndigite a terceira nota: "))
    return nota1,nota2,nota3

num1,num2,num3 = pedir_nota()
resultado= media(num1,num2,num3)
mostrar(resultado)