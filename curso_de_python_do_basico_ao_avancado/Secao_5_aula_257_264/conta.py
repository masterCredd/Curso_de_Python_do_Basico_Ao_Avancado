import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...
    
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R$ {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R$ {self.saldo:.2f} {msg}')
        print('--')
                        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attr}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R$ {valor})')
            return self.saldo
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'SAQUE NEGADO R$ {valor}')
        return self.saldo


class ContaCorrete(Conta):
    def __init__(
        self,
        agencia: int,
        conta: int,
        saldo: float = 0,
        limite: float = 0
    ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R$ {valor})')
            return self.saldo

        print('Não foi possível saca o valor desejado')
        print(f'Seu limite é R$ {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO R$ {valor}')
        return self.saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            '{self.limite!r})'
        return f'{class_name}{attr}'


if __name__ == '__main__':
    cp_1 = ContaPoupanca(111, 222, 0)
    cp_1.sacar(1)
    cp_1.depositar(1)
    cp_1.sacar(1)
    cp_1.sacar(1)

    print('###')

    cc_1 = ContaCorrete(111, 222, 0, 100)
    cc_1.sacar(1)
    cc_1.depositar(1)
    cc_1.sacar(1)
    cc_1.sacar(1)
    cc_1.sacar(1)
    cc_1.sacar(98)
    cc_1.sacar(1)

    print('###')
