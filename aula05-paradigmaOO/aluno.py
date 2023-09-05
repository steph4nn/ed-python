class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @nome.setter
    def nome(self, value: str):
        self.__nome = value

    @property
    def matriculaFormatada(self):
        matriculaString = str(self.__matricula)
        matriculaString = f'{matriculaString[:4]}.{matriculaString[4]}.{matriculaString[5:]}'
        return matriculaString
    
    def media(self):
        mediaA = 0
        for i in range(len(self.__notas)):
            mediaA += self.__notas[i]
        mediaA = mediaA/len(self.__notas)
        mediaA = round(mediaA, 2)
        return mediaA

    def adicionaNota(self, outraNota: int):
        self.__notas.append(outraNota)