#criar novas classes de desconto sem modificar a base; exemplo: desconto de fidelidade

class Desconto:
    @staticmethod
    def calcular(valor):
        return valor

class DescontoFidelidade(Desconto):
    @staticmethod
    def calcular_fidelidade(valor):
        taxa_desconto=0.05
        valor_desconto=valor*taxa_desconto
        return valor - valor_desconto

class ValorCompra:
    @staticmethod
    def pedir_valor_compra():
        try:
            compra = float(input("digite o valor da compra: "))
            return compra
        except ValueError:
            print("valores inválidos, tente novamente")
            return 0


valor_bruto=ValorCompra.pedir_valor_compra()
print("-"*30)
print(f'o valor da compra foi R${valor_bruto:.2f}')
print("-"*30)

desconto_fidelidade=DescontoFidelidade()
valor_fidelidade=DescontoFidelidade.calcular_fidelidade(valor_bruto)

print(f"Valor com Desconto Fidelidade (5%): R$ {valor_fidelidade:.2f}")
print(f"Economia: R$ {valor_bruto - valor_fidelidade:.2f}")