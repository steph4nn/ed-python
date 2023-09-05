from semaforo import Semaforo, Estado
from temporizador import Temporizador


# estadoAtual = int(input('Qual estado do semaforo? '))
# semaforo = Semaforo(Estado.verde)
# semaforo.setup(5,5,5)
# print(semaforo.__dict__)
# print(semaforo)
# semaforo.start()

s1 = Semaforo(Estado.amarelo)
s1.setup(3,2,3)
s1.start(2)