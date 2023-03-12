import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...
    
    def depositar(self, valor: float) -> float:
        """
        The depositar function adds the value of valor to the saldo attribute.
            It then calls detalhes with a string containing information about 
            the deposit.
            Finally, it returns self.saldo.
        
        :param self: Represent the instance of the class
        :param valor: float: Receive the value that will be deposited into the 
                        account
        :return: The value of self
        :doc-author: Trelent
        """
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R$ {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        """
        The detalhes function prints the current balance of the account.
            
        
        :param self: Represent the instance of the class
        :param msg: str: Pass a message to the function
        :return: None
        :doc-author: Trelent
        """
        print(f'O seu saldo é R$ {self.saldo:.2f} {msg}')
        print('--')
                        
    def __repr__(self) -> str:
        """
        The __repr__ function is used to compute the &quot;official&quot; 
        string representation of an object.
        This is how you would make an object of the class (by passing its 
        arguments to the class).
        The goal of __repr__ is to be unambiguous.
        
        :param self: Represent the instance of the class
        :return: A string that is the representation of the object
        :doc-author: Trelent
        """
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attr}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        """
        The sacar function takes a float value and subtracts it from the saldo 
        attribute.
        If the resulting value is greater than or equal to 0, 
        then the subtraction is performed and 
        the function returns self.saldo 
        (which should be equal to valor_pos_saque). If not, then an error 
        message 
        is printed out and self.detalhes(f'SAQUE NEGADO R$ {valor}') is called 
        before returning self.saldo.
        
        :param self: Represent the instance of the class
        :param valor: float: Define the value that will be withdrawn from the 
        account
        :return: A float
        :doc-author: Trelent
        """
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
        """
        The sacar function is responsible for withdrawing money from the 
        account.
        It takes a value as an argument and subtracts it from the balance, if 
        possible.
        If not, it prints a message explaining why.
        
        :param self: Represent the instance of the class
        :param valor: float: Receive the value that will be withdrawn from the 
        account
        :return: The current balance
        :doc-author: Trelent
        """
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
        """
        The __repr__ function is used to return a string representation of the 
        object.
        This function should be able to recreate an instance of the class from 
        its string representation.
        The __repr__ function is called by Python's built-in repr() and str() 
        functions, as well as by print().
        
        
        :param self: Represent the instance of the class
        :return: The class name, the attributes and their values
        :doc-author: Trelent
        """
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
