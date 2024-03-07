# Se puede importar clases y metodos de otros archivos
# como si se tratase de librerias como math o random
from .Phrase import Phrase
from .player import Player
from .ruleta import Ruleta, PremioTipoEnum


class RoundGame:
    # constructior de la clase Roundgame
    def __init__(self, numRonda: int, players: list[Player], frase: Phrase, jugadorInicio: Player):
        self.players = players
        self.numRound = numRonda
        self.frase = frase
        self.jugadorInicio = jugadorInicio

    # Funcion playRound muestra el jugador que ha ganado la ronda
    # y pasa el turno al siguiente jugador del juego
    def playRound(self):

        player = self.jugadorInicio
        while True:
            # Si ha acertado ==> True, sino False
            resultadoTurno = self.playTurn(player)
            if resultadoTurno == True:
                # Jugador ha ganado la Ronda
                player.aplyWinRound()
                # Retorna el jugador siguiente al que ha ganado
                return self.__calculateNextPlayerTurn(player)

            # Pasamos al siguiente Jugador ==> Calcular el siguiente jugador
            player = self.__calculateNextPlayerTurn(player)

    # La funcion Playturn llama al archivo ruleta.py que gira la ruleta de forma aleatoria
    # y devuelve un supuedto premio
    def playTurn(self, jugador: Player):
        """
        Método para jugar un turno con un mismo jugador
        :param jugador:
        :return: True, si gana el panel, False, si pierde el turno
        """

        # Repetir tantas veces como tiradas haga el jugador, mientras mantenga el turno
        while True:
            (tipoPremio, casilla) = Ruleta.girar()

            match tipoPremio:
                case PremioTipoEnum.BANCARROTA:
                    jugador.aplyBankrupt()
                    print("   Bancarrota")
                    return False

                case PremioTipoEnum.PIERDE_TURNO:
                    print("   Pierde Turno")
                    return False

                case PremioTipoEnum.PREMIO:
                    tipoMovimiento = jugador.goMove()
                    match tipoMovimiento:






    # Funcion __calculateNextPlayerTurn que averigua la posicion en la lista del jugador
    def __calculateNextPlayerTurn(self, playerActual: Player):
        indexPlayerActual = self.players.index(playerActual)
        if indexPlayerActual == len(self.players):
            # Estamos en el ultimo jugador de la lista
            return self.players[0]

        return self.players[indexPlayerActual + 1]

    def loadPanel(self):
        pass

    def showInfo(self):
        pass

    def showTurnInfo(self):
        pass

    def solvePanel(self):
        pass

    def guessLetter(self):
        pass
