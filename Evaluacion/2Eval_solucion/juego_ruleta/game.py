from .Phrase import Phrase
from .constantes import Constantes
from .player import HumanPlayer, ComputerPlayer, DuoPlayer, Player
from .roundgame import RoundGame


class Game:
    # Constructor de la clase Game
    def __init__(self, players: list[Player] = None):
        self.players = []
        self.lastRound = 0
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
        if not self.__loadGame():

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

        for numRonda in range(1, Constantes.TOTAL_ROUNDS + 1):
            # Obtener la frase
            frase = Phrase.getPhrase()
            ronda = RoundGame(numRonda, self.players, frase, playerIniciaRonda)
            playerIniciaRonda = ronda.playRound()

    def __endGame(self):
        """
        Encargado de finalizar el juego
        :return:
        """
        # MOSTRAR EL GANADOR

    def __loadGame(self):
        """
        Este metodo...
        :return: True si existe partida guarda, y por tanto el juego se configura en base a esta partida. False en caso contrario
        """

        # 1. Verificar si existe ruta, y dentro de la ruta existe un fichero. SINO SALIR FALSO

        # 2. Verificar tipo. Si es CSV llamar método CSV, sino llamar método JSON

        # Retorno TRUE, indicando que el juego parte desde una partida guardada

        pass

    def __loadGameCSV(self):
        """

        :return:
        """

        # 1. Revivar si existe un fichero en la ruta y del tipo adecuado (CSV)

        # 2. Llamar Lector CSVReader del módulo de Python. Obtener información de las columnas
        # 2. -> Construir los players, construir la ronda, ronda_actual
        self.lastRound

        pass

    def __loadGameJson(self):
        pass

    def saveGame(self):
        pass
