import conta
import pessoa


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoa.Pessoa] | None = None,
            contas: list[conta.Conta] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta) -> bool:
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente) -> bool:
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta) -> bool:
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta) -> bool:
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(
                self,
                cliente: pessoa.Pessoa,
                conta: conta.Conta
            ) -> bool:
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c_1 = pessoa.Cliente('Luiz', 30)
    cc_1 = conta.ContaCorrete(111, 222, 0, 0)
    c_1.conta = cc_1

    c_2 = pessoa.Cliente('Maria', 30)
    cp_1 = conta.ContaCorrete(112, 223, 100)
    c_2.conta = cp_1

    banco = Banco()
    banco.clientes.extend([c_1, c_2])
    banco.contas.extend([cc_1, cp_1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c_1, cc_1):
        cc_1.depositar
        c_1.conta.depositar(100)
        print(c_1.conta)
