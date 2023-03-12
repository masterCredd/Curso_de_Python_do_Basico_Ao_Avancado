import conta
import pessoa


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoa.Pessoa] | None = None,
            contas: list[conta.Conta] | None = None
    ) -> None:
        """
        The __init__ function is the constructor for the Banco class.
        It takes three optional arguments: agencias, clientes, and contas.
        If any of these are not provided, they will be initialized to an empty 
        list.
        
        :param self: Represent the instance of the class
        :param agencias: list[int] | None: Create a list of agencies
        :param clientes: list[pessoa.Pessoa] | None: Define the clientes 
        attribute of banco
        :param contas: list[conta.Conta] | None: Create a list of conta objects
        :return: None
        :doc-author: Trelent
        """
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta) -> bool:
        """
        The _checa_agencia function checks if the account's agency is in the 
        bank's list of agencies.
            
        
        :param self: Represent the instance of the class
        :param conta: Get the agencia attribute of the conta object
        :return: True or false
        :doc-author: Trelent
        """
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente) -> bool:
        """
        The _checa_cliente function checks if the cliente is in the list of 
            clients.
            Args:
                cliente (str): The name of a potential client.
            Returns:
                bool: True if the client exists, False otherwise.
        
        :param self: Represent the instance of the class
        :param cliente: Check if the client is in the list of clients
        :return: A boolean value
        :doc-author: Trelent
        """
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta) -> bool:
        """
        The _checa_conta function checks if the account is in the list of 
            accounts.
            Args:
                conta (int): The account number to be checked.
        
        :param self: Represent the instance of the class
        :param conta: Check if the account exists in the list of accounts
        :return: A boolean
        :doc-author: Trelent
        """
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta) -> bool:
        """
        The _checa_se_conta_e_do_cliente function checks if the account 
        belongs to the client.
            Args:
                cliente (Cliente): The Client object.
                conta (Conta): The Account object.
        
        :param self: Represent the instance of the class
        :param cliente: Check if the account is from the client
        :param conta: Check if the account is from the client
        :return: True or false
        :doc-author: Trelent
        """
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(
                self, 
                cliente: pessoa.Pessoa, conta: conta.Conta) -> bool:
        """
        The autenticar function checks if the client is authorized to access 
        the account.
            Args:
                cliente (pessoa.Pessoa): The person who wants to access an 
                account.
                conta (conta.Conta): The account that will be accessed by a
                person.
        
        :param self: Represent the instance of the class
        :param cliente: pessoa.Pessoa: Check if the client is registered in 
        the bank
        :param conta: conta.Conta: Check if the account is valid
        :return: A bool, but it is not used anywhere
        :doc-author: Trelent
        """
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        """
        The __repr__ function is one of several ways to provide a nicer string 
        representation for your objects.
        The __repr__ function should return a string that, if evaluated in 
        Python, would recreate the object.
        This means that it should include all information necessary to 
        recreate the object.
        
        :param self: Represent the instance of the class
        :return: A string representation of the object
        :doc-author: Trelent
        """
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
