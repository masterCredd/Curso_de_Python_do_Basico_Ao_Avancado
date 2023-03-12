from threading import Thread
from time import sleep


class MeuThread(Thread):
    """Exemplo de threads"""
    
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo
        super().__init__()
    
    def run(self):
        sleep(self.tempo)
        print(self.texto)


def vai_demorar(texto: str, tempo: int):
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

        
t_1 = MeuThread('Thread 1', 5)
t_1.start()
t_2 = MeuThread('Thread 1', 5)
t_2.start()
t_3 = MeuThread('Thread 1', 5)
t_3.start()
for i in range(20):
    print(i)
    sleep(1)
