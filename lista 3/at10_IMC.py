#pedindo o peso
peso=float(input("digite seu peso: (Kg) "))

#pedindo altura
altura=float(input("digite sua altura: (m) "))

#calculando IMC
imc=peso/(altura**2)

#verificando faixa de IMC
resultado = (imc >= 18.5) and (imc <= 24.9)

print(f"o imc está na faixa saudável? {resultado}")