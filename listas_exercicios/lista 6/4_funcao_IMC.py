#criando função calcular imc
def calcular_imc(peso,altura):
    return peso/(altura**2)

#criando função exibir faixa imc
def exibir_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc <= 24.9:
        return "peso normal"
    elif imc <=29.9:
        return "sobrepeso"
    else:
        return "obesidade"

#atribuindo peso e altura para calcular o imc
peso_altura=calcular_imc(70,1.75)

#chamando a função para exibir o imc
print(exibir_imc(peso_altura))
