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

    def elemento(self, posicao:int)-> any:

        try:
            assert posicao >0 and posicao <= len(self),'posicao invalida'        
            return self.__array[posicao-1]
            
        except AssertionError:

            raise PilhaException('posicao invalida')
