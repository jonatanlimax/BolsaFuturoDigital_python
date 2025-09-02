def par_impar():
    x=int(input("digite um número: "))
    if x % 2 == 0:
        return "par"
    else:
        return "impar"

print(par_impar())