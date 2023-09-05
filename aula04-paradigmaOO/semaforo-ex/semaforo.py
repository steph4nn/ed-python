from temporizador import Temporizador
from enum import Enum

class Estado(Enum):
    vermelho = 1
    amarelo =2 
    verde = 3

class Semaforo:
    def __init__(self, estadoInicial:Estado = Estado.vermelho):
        self.__estadoAtual = estadoInicial
        self.__timer = Temporizador()
        self.__tempoDeTransicao ={Estado.verde:20, \
                                Estado.amarelo:5,  \
                                Estado.vermelho:10}

    @property
    def estadoAtual(self) ->Estado:
        return self.__estadoAtual
    
    @property
    def tempoDeTransicao(self) ->dict:
        # Retornando uma cópia do objeto, e não sua referência
        # isso é importante para que o objeto não seja alterado
        return self.__tempoDeTransicao
    
    def __str__(self):
        return f'''
        +-------+
        |  ({"X" if self.__estadoAtual == Estado.vermelho else " "})  |
        |  ({"X" if self.__estadoAtual == Estado.amarelo else " "})  |
        |  ({"X" if self.__estadoAtual == Estado.verde else " "})  |
        +-------+

        O sinal esta {self.__estadoAtual}!
        
        '''
    def setup(self, tempoVermelho:int, tempoAmarelo:int, tempoVerde:int):
        '''
        Método que permite ajustar o tempo dos estados do semáforo.
        Aceita um tempo em segundos entre 1 e 59

        Argumentos
        ----------
        tempoVermelho(int): tempo em segundos de permanência no vermelho
        tempoAmarelo(int): tempo em segundos de permanência no amarelo
        tempoVerde(int): tempo em segundos de permanência no verde
        '''
        if tempoVermelho <1 or tempoVermelho >59:
            return
        elif tempoAmarelo <1 or tempoAmarelo >59:
            return
        elif tempoVerde <1 or tempoVerde >59:
            return

        self.__tempoDeTransicao[Estado.vermelho] = tempoVermelho
        self.__tempoDeTransicao[Estado.amarelo] = tempoAmarelo
        self.__tempoDeTransicao[Estado.verde] = tempoVerde
    
    def __proximoEstado(self):
        if self.__estadoAtual == Estado.vermelho:
            self.__estadoAtual = Estado.verde
        elif self.__estadoAtual== Estado.verde:
            self.__estadoAtual = Estado.amarelo
        else:
            self.__estadoAtual = Estado.vermelho
    

    def start(self,numCiclos:int):
        '''
        Método que inicia o ciclo de funcionamento do semáforo.

        Argumentos
        ----------
        numCiclos(int): número de ciclos que o semáforo deve executar.
                        Cada ciclo é constutuído pela passagem por 3 estados:
                        vermelho, amarelo e verde
        '''
        for i in range(numCiclos*3):
                print(self) 
                self.__timer.duracao = self.__tempoDeTransicao[self.__estadoAtual]
                self.__timer.ativar()
                self.__proximoEstado()
                print()


