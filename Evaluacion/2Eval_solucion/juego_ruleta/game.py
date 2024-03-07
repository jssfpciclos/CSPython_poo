from .player import HumanPlayer, ComputerPlayer, DuoPlayer, Player
from .constantes import Constantes
from .roundgame import RoundGame
from .Phrase import Phrase


class Game:
    # Constructor de la clase Game
    def __init__(self, players: list[Player] = None):
        self.players = []
        if players is not None:
            self.players = players

    # Funcion start de comienzo el juego
    def start(self):
        self.__initGame()
        self.__playRounds()
        self.__endGame()

    # Funcion __initGame, mensaje de bienvenida al juego. Pedira cuantos jugadores participan
    def __initGame(self):
        """
        Inicializa el juego, creando los jugadores y inicializando las variables
        :return:
        """
        print("---BIENVENIDO A LA RULETA DE LA SUERTE---")

        # Construcciones Jugadores
        if len(self.players) is 0:
            njugadores = int(input("tecleee numero de jugadores: "))

            for numJugador in range(1, int(njugadores) + 1):
                # Qué tipo de Jugador
                tipo = input(f"Indique el tipo (1-Humano, 2-Computadora, 3-Duo): ")
                # Dependiendo del tipo de jugador, humano o computadora se carga una opcion u otra.
                match tipo:
                    case "1":
                        nombre = input(f"Introduzca el nombre del Jugador{numJugador}: ")
                        humanPlayer = HumanPlayer(nombre)
                        self.players.append(humanPlayer)

                    case "2":
                        computerPlayer = ComputerPlayer(f"Computadora{numJugador}")
                        self.players.append(computerPlayer)

                    case "3":
                        nombre = input(f"Introduzca el nombre del Equipo-{numJugador}: ")
                        duoPlayer = DuoPlayer(nombre)
                        self.players.append(duoPlayer)

                    case _:
                        print("Tipo de Jugador no válido")

    def __playRounds(self):
        """
        Encargado de ejecutar el jugar cada una de las rondas del juego
        :return:
        """
        # ===== INICIA EL JUEGO ====
        playerIniciaRonda = self.players[0]

        for numRonda in range(1, Constantes.TOTAL_ROUNDS+1):
            # Obtener la frase
            frase = Phrase.getPhrase()
            ronda = RoundGame(numRonda,self.players,frase,playerIniciaRonda)
            playerIniciaRonda = ronda.playRound()

        # MOSTRAR EL GANADOR

    def __endGame(self):
        """
        Encargado de finalizar el juego
        :return:
        """

    def loadGame(self):
        pass

    def saveGame(self):
        pass
