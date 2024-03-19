from abc import ABC, abstractmethod
from enum import IntEnum


class TipoJugadorEnum(IntEnum):
    # Clase Enumerate para poder elegir una opcion. Se importa con enum de IntEnum
    HUMANO = 1
    COMPUTADORA = 2
    EQUIPO = 3


class JugadorTipoMovientoEnum(IntEnum):
    LETRA = 0
    RESOLVER = 1
    PASO = 2


class Player(ABC):  # Clase padre Player
    # constructor de la clase padre
    def __init__(self, name, tipo: TipoJugadorEnum):
        self.name = name
        self.prizeMoney = 0
        self.prizeMoneyRound = 0
        self.tipo = tipo

    # Funcion aplyBankrupt aparece cuando el jugador cae en quiebra en la ruleta,
    # en tal caso la bolsa de ese jugador en la ronda vuele a cero
    def aplyBankrupt(self):
        self.prizeMoneyRound = 0

    # Funcion addPrizeRound acumula las ganancias del jugador en la ronda
    def addPrizeRound(self, cantidad: int):
        self.prizeMoneyRound += cantidad

    # Funcion aplyWinRound acumula la ganancia del ganador de la ronda en su bolsa personal
    # y vuelve a iniciar la bolsa de la ronda a 0
    def aplyWinRound(self):
        self.prizeMoney += self.prizeMoneyRound
        self.prizeMoneyRound = 0

    # Funcion metodo magico __eq__ que compara si es un jugador u otro de la lista
    def __eq__(self, other: 'Player'):
        return self.name == other.name

    def __str__(self):
        return f"{self.name} - Ronda:{self.prizeMoneyRound} Total:{self.prizeMoney}"

    @abstractmethod  # Metodo abstracto hay que importarlo de abc abstractmethod
    def goMove(self) -> JugadorTipoMovientoEnum:
        pass

    @abstractmethod  # Metodo abstracto hay que importarlo de abc abstractmethod
    def goResolver(self, frase: str):
        pass

    @abstractmethod  # Metodo abstracto hay que importarlo de abc abstractmethod
    def goGuestLetter(self):
        pass


class HumanPlayer(Player):  # Clase HumanPlayer con herencia de la clase Padre Player
    # Constructor de la clase HumanPlayer
    def __init__(self, name: str):
        super().__init__(name, TipoJugadorEnum.HUMANO)

    def goMove(self) -> JugadorTipoMovientoEnum:

        while True:
            eleccion = input(">> Indique movimiento Letra(Enter), 1-Resolver, 2-Paso: ")
            match eleccion:
                case "1":
                    # Resolver
                    return JugadorTipoMovientoEnum.RESOLVER
                case "2":
                    # paso
                    return JugadorTipoMovientoEnum.PASO
                case "":
                    # Indicar letra
                    return JugadorTipoMovientoEnum.LETRA

                case _:
                    # Opción no valida
                    print("  --- opción no válida. Vuelve a indicar una opción correcta")

    def goResolver(self, frase: str):
        frase_usuario = input(">> Indique la frase completa: ")

        return frase_usuario.upper() == frase.upper()

    def goGuestLetter(self):

        letra = input("  Indique una letra: ")
        return letra.upper()


class ComputerPlayer(Player):  # Clase ComputerPlayer con herencia de la clase Padre Player

    # constructor de la clase ComputerPlayer
    def __init__(self, name: str):
        super().__init__(name, TipoJugadorEnum.COMPUTADORA)

    def goMove(self):
        pass

    def goResolver(self, frase: str):
        pass

    def goGuestLetter(self):
        pass


class DuoPlayer(Player):

    def __init__(self, name):
        super().__init__(name, TipoJugadorEnum.EQUIPO)

    def goMove(self):
        pass

    def goResolver(self, frase: str):
        pass

    def goGuestLetter(self):
        pass
