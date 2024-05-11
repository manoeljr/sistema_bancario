menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
=>>>> """

__LIMITE_SAQUES = 3

saldo = 0
limite = 500
extrato = ""
numero_saques = 0


while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Valor depositado: {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Valor a ser sacado: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= __LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou, você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou, valor do saque excede o limite.')
        elif excedeu_saques:
            print('Operação falhou, número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou, valor informado é inválido.')

    elif opcao == '3':
        print('\n============== EXTRATO ==========================')
        print('Não foram realizados movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===================================================')
    elif opcao == "4":
        break
    else:
        print('Operação inválida, tente novamente.')
