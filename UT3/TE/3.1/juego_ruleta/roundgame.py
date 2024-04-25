# Se puede importar clases y metodos de otros archivos
# como si se tratase de librerias como math o random
from .Phrase import Phrase
from .constantes import Constantes
from .player import *
from .ruleta import Ruleta, PremioTipoEnum
from .config import Config


class RoundGame:
    # constructior de la clase Roundgame
    def __init__(self, numRonda: int, players: list[Player], panel: Phrase, jugadorInicio: Player):
        self.players = players
        self.numRound = numRonda
        self.panel = panel
        self.jugadorInicio = jugadorInicio
        self.letrasDichas = []

    def playRound(self):
        """
        Muestra el jugador que ha ganado la ronda y pasa el turno al siguiente jugador del juego
        :return:
        """

        player = self.jugadorInicio
        while True:
            # Si ha acertado ==> True, sino False
            resultadoTurno = self.__playTurn(player)
            if resultadoTurno == True:
                print(f"  Enhorabuena {player.name}, has ganado la ronda. Has acumulado {player.prizeMoneyRound:.2f} "
                      f"en la ronda ")
                # Hacemos firme el dinero de la ronda a cada jugador
                for p in self.players:
                    p.aplyWinRound()

                print("  Resumen de totales:\n")
                for p in self.players:
                    print(f"  {p.name} acumula .... {p.prizeMoney:.2f}")

                # Retorna el jugador siguiente al que ha ganado
                return self.__calculateNextPlayerTurn(player)

            # Pasamos al siguiente Jugador ==> Calcular el siguiente jugador
            player = self.__calculateNextPlayerTurn(player)

    # La funcion Playturn llama al archivo ruleta.py que gira la ruleta de forma aleatoria
    # y devuelve un supuedto premio
    def __playTurn(self, jugador: Player):
        """
        Método para jugar un turno con un mismo jugador
        :param jugador:
        :return: True, si gana el panel, False, si pierde el turno
        """

        # Repetir tantas veces como tiradas haga el jugador, mientras mantenga el turno
        while True:
            self.showTurnInfo(jugador)

            (tipoPremio, casilla) = Ruleta.girar()

            match tipoPremio:
                case PremioTipoEnum.BANCARROTA:
                    jugador.aplyBankrupt()
                    print(f"    Nueva tirada. Bancarrota. LO SIENTE. PIERDES TODO EL DINERO EL LA RONDA")
                    return False

                case PremioTipoEnum.PIERDE_TURNO:
                    print(f"    Nueva tirada. PIERDE TURNO. LO SIENTE. HAS PERDIDO EL TURNO")
                    return False

                case PremioTipoEnum.PREMIO:
                    print(f"    Nueva tirada. Juegas por {casilla:.2f}. Indica movimiento...")
                    tipoMovimiento = jugador.goMove()
                    match tipoMovimiento:
                        case JugadorTipoMovientoEnum.RESOLVER:
                            resultado = jugador.goResolver(self.panel.frase)
                            if resultado:
                                # Incrementar al dinero de la ronda la recompensa
                                jugador.addPrizeRound(Config.recompensa_panel)

                            return True

                        case JugadorTipoMovientoEnum.PASO:
                            return False

                        case JugadorTipoMovientoEnum.LETRA:

                            letra = ""
                            while True:
                                letra = jugador.goGuestLetter()
                                letra = letra.upper()
                                # Validación de si es posible esa letra

                                # 2. Si letra ya dicha, invalido
                                if letra in self.letrasDichas:
                                    print(f" X no puede elegir la letra {letra}, ya ha sido elegida anteriormente.")
                                    continue

                                # 1. Si es vocal, y no tiene saldo, invalido
                                if letra in Constantes.VOCALES and jugador.prizeMoneyRound < Config.vocal_precio:
                                    print(" X no puede elegir Vocal, saldo insuficiente.")
                                    continue

                                # Agregamos a letras dichas
                                self.letrasDichas.append(letra)

                                # 3. Si letra no existe en panel, Pierde Turno
                                if letra not in self.panel.frase:
                                    print(f" X La letra no está en la frase. Pierde turno")
                                    return False

                                break  # Letra es válida. Salgo del While

                            if letra in Constantes.VOCALES:
                                jugador.addPrizeRound(Config.vocal_precio * -1)
                                print(f"  Has comprado vocal. Pagas {Config.vocal_precio:.2f}. Te queda "
                                      f"{jugador.prizeMoneyRound:.2f}")

                            # Saber cuantas veces la letra está dentro del panel
                            ocurrencias = self.panel.frase.count(letra)
                            premio_tirada = ocurrencias * casilla

                            print(f"\n  La {letra} está {ocurrencias} veces en la frase. Ganas {premio_tirada:.2f}")
                            jugador.addPrizeRound(premio_tirada)

                            # El turno continua, hasta salir del While

            print(" __________________________________________________________________  ")


    # Funcion __calculateNextPlayerTurn que averigua la posicion en la lista del jugador
    def __calculateNextPlayerTurn(self, playerActual: Player):
        indexPlayerActual = self.players.index(playerActual)
        if indexPlayerActual == len(self.players)-1:
            # Estamos en el ultimo jugador de la lista
            return self.players[0]

        return self.players[indexPlayerActual+1]

    def __oscurecerFrase(self, frase: str, letrasDichas: list[str]):
        fraseOscurecida = ""
        for letra in frase.upper():
            letraOculta = ""
            if letra in letrasDichas:
                letraOculta = letra
            else:
                if letra in Constantes.ABECEDARIO:
                    letraOculta = "_"
                elif letra in Constantes.SIGNOS:
                    letraOculta = letra

            fraseOscurecida += letraOculta

        return fraseOscurecida

    def loadPanel(self):
        pass

    def showInfo(self):
        pass

    def showTurnInfo(self, jugadorTurno: Player):

        print(f" --------- TURNO DE {jugadorTurno.name} ----------------------")
        print(f"           Dinero acumulado en ronda: {jugadorTurno.prizeMoneyRound:.2f}\n")
        print(
            f"           {self.__oscurecerFrase(self.panel.frase, self.letrasDichas)}      Letras Dichas: {self.letrasDichas}")
        print("\n")

    def solvePanel(self):
        pass

    def guessLetter(self):
        pass
