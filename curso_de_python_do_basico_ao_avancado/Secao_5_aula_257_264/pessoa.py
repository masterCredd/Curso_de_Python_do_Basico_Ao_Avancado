
import conta


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attr}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: conta.Conta | None = None


if __name__ == '__main__':
    c_1 = Cliente('Luiz', 30)
    c_1.conta = conta.ContaCorrete(111, 222, 0, 0)

    print(c_1)
    print(c_1.conta)

    c_2 = Cliente('Maria', 18)
    c_2.conta = conta.ContaPoupanca(112, 223, 100)

    print(c_2)
    print(c_2.conta)
