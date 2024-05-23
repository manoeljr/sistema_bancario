from classes.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque__name__]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques >= self.limite_saques

        if excedeu_limite:
            print('Deu ruim')
        elif excedeu_saques:
            print('Não tem jeito')
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titula:\t{self.cliente.nome}
        """
