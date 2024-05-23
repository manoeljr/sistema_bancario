from funcoes.funcao import menu
from classes.deposito import Deposito


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            Deposito.depositar(clientes)