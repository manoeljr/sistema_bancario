def menu():
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuario
        [nc] Nova Conta
        [lc] Listat Contas
        [q] Sair
    =>>>> """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${saldo:.2f}\n'
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou o valor informado é invalido.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
        print('Saque realizado com sucesso!')
    else:
        print('Operação falhou, valor informado é inválido.')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('\n============== EXTRATO ==========================')
    print('Não foram realizados movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('===================================================')

def criar_usuario(usuarios):
    cpf = input('digite o cpf:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuario com esse cpf.')
        return
    nome = input('Digite o nome:')
    data_nascimento = input('Digite a data do seu nascimento')
    endereco = input('Informe o endereço')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso.")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o cpf')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Conta criada com sucesso.')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print('Usuario não encontrado, fluxo de criação de conta encerrado')

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["nome"]}
        """
        print('=' * 100)
        print(linha)
