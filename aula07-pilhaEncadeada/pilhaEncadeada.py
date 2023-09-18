import numpy as np

class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class No:
    def __init__(self,carga:any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self):
        return self.__carga
    
    @property
    def prox(self):
        return self.__prox
    
    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga
    
    @prox.prox
    def prox(self, novoProx):
        self.__prox= novoProx

    def __str__(self):
        return f'{self.__carga}'   

class PilhaEncadeada:

    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
        

    def estaVazia(self)->bool:
        return self.__topo == None
    
    def __len__(self)-> int:
        return self.__tamanho

    def elemento(self, posicao:int)-> any:

        try:
            assert posicao >0 and posicao <= len(self),'posicao invalida'        
            cursor = self.__topo
            
            contador  = 1
            while (cursor is not None):
                if contador == posicao:
                    return cursor.carga
                cursor = cursor.prox
                contador +=1
        except AssertionError as ae:
            raise PilhaException(ae)

    def busca(self, key:any)->int:
        if (self.estaVazia()):
            raise PilhaException(f'A chave {key} não está presente na pilha')
        
        contador = 1
        cursor = self.__topo
        while (cursor is not None):
            if cursor == key:
                return contador
            cursor = cursor.prox
            contador +=1
        raise PilhaException(f'A chave {key} não está presente na pilha')

    def topo(self)->any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        return self.__topo.carga
    
    def empilha(self, carga:any):
        novo = No(carga)
        novo.prox = self.__topo
        self.__topo=novo
        self.__tamanho +=1
    
    def desempilha(self)->any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        carga = self.__topo.carga
        self.__topo = self.__topo.prox
        self.__tamanho -=1
        return carga

    def __str__(self)->str:
        s = '[ '
        cursor = self.__topo
        while (cursor is not None):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]<-topo'
        return s

    