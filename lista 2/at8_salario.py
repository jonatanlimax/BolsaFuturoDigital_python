#pedindo o salario
salario=int(input("digite seu salario: "))

#verificando se está entre 2000 e 5000
resultado = (salario >= 2000) and (salario <= 5000)

#verificando se é igual a 10000
resultado2 = salario == 10000

print(f"o salario está entre 2000 e 5000? {resultado}")
print(f"o salario é igual a 10000? {resultado2}")