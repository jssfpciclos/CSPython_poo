import random
from enum import IntEnum


class PremioTipoEnum(IntEnum):
    BANCARROTA = -1,
    PIERDE_TURNO = 0,
    PREMIO = 99


class Ruleta:
    __premios = [100, 50, 100, 150, 50, 200, 250, 50, 100, 150, 300,
                 -1, 400, 0, 500, 200, 100, 50, 250, 150, 100, 50, 200]

    # metodo estatico que devuelve un premio al azar
    @staticmethod
    def girar() -> tuple[PremioTipoEnum, int]:

        casilla = random.choice(Ruleta.__premios)
        match casilla:
            case -1:
                return (PremioTipoEnum.BANCARROTA, 0)
            case 0:
                return (PremioTipoEnum.PIERDE_TURNO, 0)
            case _:
                return (PremioTipoEnum.PREMIO, casilla)
