
import conta


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        """
        The __init__ function is called when the object is created.
        It sets up the initial state of the object.
        
        :param self: Represent the instance of the class
        :param nome: str: Set the name of the object
        :param idade: int: Define the type of data that will be passed to the 
        function
        :return: None
        :doc-author: Trelent
        """
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        """
        The nome function returns the name of the person.
        
        :param self: Represent the instance of the class
        :return: A string
        :doc-author: Trelent
        """
        
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """
        The nome function sets the nome attribute of a Pessoa object.
            Args:
                nome (str): The name to be set for the Pessoa object.
            Returns:
                None
        
        :param self: Represent the instance of the class
        :param nome: str: Define the type of data that will be passed to the 
        function
        :return: None
        :doc-author: Trelent
        """
        self._nome = nome

    @property
    def idade(self) -> int:
        """
        The idade function returns the age of a person.
        
        :param self: Represent the instance of the class
        :return: The age of a person
        :doc-author: Trelent
        """
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        """
        The idade function sets the idade attribute of a Pessoa object.
            Args:
                idade (int): The age of the person.
        
        
        :param self: Represent the instance of the class
        :param idade: int: Define the type of data that will be passed to the 
        function
        :return: None
        :doc-author: Trelent
        """
        self._idade = idade

    def __repr__(self) -> str:
        """
        The __repr__ function is used to compute the &quot;official&quot; 
        string representation of an object.
        This is how you would make an object of the class:
            obj = MyClass(attr='value')
        
        :param self: Represent the instance of the class
        :return: A string that is the representation of the object
        :doc-author: Trelent
        """
        class_name = type(self).__name__
        attr = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attr}'


class Cliente(Pessoa):
    
    def __init__(self, nome: str, idade: int) -> None:
        """
        The __init__ function is the constructor for the class.
        It initializes all of the attributes of a Cliente object, including
        the superclass's attributes. It also sets self.conta to None, since no 
        cliente has a conta yet.
        
        :param self: Represent the instance of the class
        :param nome: str: Set the name of the client
        :param idade: int: Set the age of the client
        :return: None, so the return type is none
        :doc-author: Trelent
        """
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
