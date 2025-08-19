# Entrada do usuário
n = int(input("Digite um número: "))

print(f"Números primos até {n}:")

# começa do 2, pois 0 e 1 não são primos
for num in range(2, n + 1):
    eh_primo = True
    for i in range(2, num):
        # encontrou divisor
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(num)