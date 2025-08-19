#5.Tabuada: Peça um número e exiba sua tabuada de 1 a 10.

#socilitar o número ao usuário
while True:
    num=int(input("digite um número ou digite 0 para sair: "))
    if num != 0:
        for n in range(1,11):
            print(f"{num} x {n} = ",num*n,)

    else:
        print("obrigado por usar minha tabuada! até logo!")
        break


