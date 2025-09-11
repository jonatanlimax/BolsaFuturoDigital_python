#lista de contas
contas=[
    {"conta":1,"titular":"Jonatan","saldo":1000},
    {"conta":2,"titular":"Carina","saldo":2000},
    {"conta":3,"titular":"David","saldo":3000}
        ]

#listando todas as contas
for conta in contas:
    titular = conta["titular"]
    saldo = conta["saldo"]
    n_conta=conta["conta"]
    print(f"Conta: {n_conta} | Titular: {titular} | saldo R${saldo:.2f}")

#pedindo a conta de origem da transferência
op = int(input("Digite qual conta de origem: "))
for conta in contas:
    if conta["conta"]==op:
        conta_origem=conta
        print(f"Titular: {conta["titular"]} | saldo R${conta["saldo"]:.2f}")

        #pedindo o valor da transferência
        valor=float(input("Digite o valor que deseja transferir: "))
        conta["saldo"]-=valor
        print(conta["titular"], conta["saldo"])

        #pedindo a conta de destino
        conta_destino=int(input("Digite qual conta de destino: "))
        for cont in contas:
            if cont["conta"]==conta_destino:
                conta_destino=cont
                cont["saldo"]+=valor
                print(cont["titular"], cont["saldo"])




