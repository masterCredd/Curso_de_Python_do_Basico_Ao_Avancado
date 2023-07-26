from threading import Lock, Thread
from time import sleep


class MeuThread(Thread):
    """Exemplo de threads"""
    
    def __init__(self, texto: str, tempo: int) -> None:
        """
        The __init__ function is called when the object is created.
        It sets up the initial state of the object.
        
        
        :param self: Represent the instance of the object itself
        :param texto: str: Set the text of the label
        :param tempo: int: Set the time in seconds that the message will be
        displayed
        :return: Nothing
        :doc-author: Trelent
        """
        self.texto = texto
        self.tempo = tempo
        super().__init__()
    
    def run(self) -> None:
        sleep(self.tempo)
        print(self.texto)


def vai_demorar(texto: str, tempo: int) -> None:
    """
    The vai_demorar function prints a text after sleeping for a given amount
        of time.
        
        Args:
            texto (str): The string to be printed.
            tempo (int): The number of seconds the function will sleep before
            printing the string.
    
    
    :param texto: str: Define the text that will be printed
    :param tempo: int: Define how long the function will wait before printing
                    the texto: str parameter
    :return: The value of the print function
    :doc-author: Trelent
    """
    sleep(tempo)
    print(texto)
    

class Ingressos(object):
    """docstring for Ingressos."""
    def __init__(self, estoque: int):
        """
        The __init__ function is called when the object is created.
        It sets up the initial state of the object.
        
        
        :param self: Represent the instance of the class
        :param estoque: int: Set the initial stock of the item
        :return: Nothing
        :doc-author: Trelent
        """
        self.estoque = estoque
        self.lock = Lock()
        
    def comprar(self, quantidade: int) -> None:
        """
        The comprar function is responsible for buying tickets.
        It takes a quantity as an argument and checks if there are enough
        tickets in stock.
        If so, it sleeps for 1 second to simulate the time spent on the
        purchase process, then subtracts the amount from stock and prints a
        message with how many tickets were bought and how many are left in
        stock.
        :param self: Represent the instance of the class
        :param quantidade: int: Define the number of tickets that will be
        purchased
        :return: Nothing
        :doc-author: Trelent
        """
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return
        sleep(1)
        self.estoque -= quantidade
        print(
            f'Você comprou {quantidade} ingresso(s).'
            f'Ainda temos {self.estoque} em estoque.')
        self.lock.release()
    
        
t_1 = MeuThread('Thread 1', 5)
t_1.start()
t_2 = MeuThread('Thread 1', 5)
t_2.start()
t_3 = MeuThread('Thread 1', 5)
t_3.start()
for i in range(20):
    print(i)
    sleep(1)


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    print(ingressos.estoque)