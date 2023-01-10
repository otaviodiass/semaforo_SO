from threading import Thread #Importação da class Thread
from threading import Semaphore #Importação da class Semaphore
from time import sleep #Importação da funcão sleep

contador = 0
obj = Semaphore() #A classe Semaphore faz o controle de threads que podem acessar um recurso simultaneamente

class Processo(Thread):  #Class Processo 
    def __init__(self,p): #Construtor da classe Processo
        Thread.__init__(self) #Construtor da classe Thread
        self.p=p

    def run(self): #Método contendo o que será executado por cada thread
        
        global contador

        while True:
            obj.acquire() #Este método realiza o procedimento de bloqueio da região crítica (semáforo bloqueado)
            print(f'Processo: {self.p}, entrou na região crítica, contador: {contador}')
            contador += 1 #Mostra a sequêcia de entrada e saída dos processos 
            print(f'Processo: {self.p}, saiu na região crítica, contador: {contador}')
            obj.release() #Este método desbloqueia a região crítica (semáforo liberado)
            sleep(1) 

for i in range(10): #for responsável por criar 10 threads e inicializa-lás
    proc = Processo(i)
    proc.start()