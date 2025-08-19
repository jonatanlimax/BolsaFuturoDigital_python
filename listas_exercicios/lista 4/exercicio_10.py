
#10. Soma dos ímpares: Calcule a soma de todos os números ímpares entre 1 e 100.

soma=0
for n in range(1,101):
    if n % 2 != 0:
        soma+=n
print(f"a soma de todos os números ímpares entre 1 e 100 é {soma}")
