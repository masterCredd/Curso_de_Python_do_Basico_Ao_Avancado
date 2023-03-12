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
        
t_1 = MeuThread('Thread 1', 5)
t_1.start()
t_2 = MeuThread('Thread 1', 5)
t_2.start()
t_3 = MeuThread('Thread 1', 5)
t_3.start()
for i in range(20):
    print(i)
    sleep(1)
