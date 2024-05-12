from funcoes.funcao import menu, depositar, sacar, exibir_extrato, criar_usuario, criar_conta, listar_contas

__LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []


while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "s":
        valor = float(input("Valor a ser sacado: "))
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=__LIMITE_SAQUES,
        )
    elif opcao == 'e':
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == 'nu':
        criar_usuario(usuarios)
    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == 'lc':
        listar_contas(contas)
    elif opcao == "q":
        break
    else:
        print('Operação inválida, tente novamente.')
