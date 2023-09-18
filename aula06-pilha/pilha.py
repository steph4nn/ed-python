import numpy as np

class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)


class Pilha:

    def __init__(self,qtde=10):
        self.__array = np.full(qtde,None,dtype=object)
        self.__topo = -1

    def estaVazia(self)->bool:
        return self.__topo == -1
    
    def __len__(self)-> int:
        return self.__topo +1

    def elemento(self, posicao:int)-> any:

        try:
            assert posicao >0 and posicao <= len(self),'posicao invalida'        
            return self.__array[posicao-1]
        except AssertionError as ae:
            raise PilhaException(ae)

    def busca(self, key:any)->int:
        for i in range(len(self)):
            if self.__array[i] == key:
                return i+1
        raise PilhaException(f'A chave {key} não está presente na pilha')

    def topo(self)->any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        return self.__array[self.__topo]
    
    def empilha(self, carga:any):
        if self.__topo == len(self.__array)-1:
            raise PilhaException('Pilha cheia')
        self.__topo += 1
        self.__array[self.__topo] = carga
    
    def desempilha(self)->any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        carga = self.__array[self.__topo]
        self.__topo -=1
        return carga

    def __str__(self)->str:
        s = '[ '
        for i in range(len(self)):
            s += f'{self.__array[i]}, '
        s = s.rstrip(', ')
        s += ' ]<-topo'
        return s