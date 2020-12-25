from random import randint
class cacular:
    def __init__ (self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property 
    def valor1(self: object) -> int:
        return self.__valor1

    
