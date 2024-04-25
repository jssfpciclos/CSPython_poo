import csv
import json
import os.path

from .Phrase import Phrase
from .constantes import Constantes
from .player import HumanPlayer, ComputerPlayer, DuoPlayer, Player, TipoJugadorEnum
from .roundgame import RoundGame
from .config import Config


class Game:
    # Constructor de la clase Game
    def __init__(self, players: list[Player] = None):
        self.players = []
        self.lastRound = 0
        self.lastTurnIndex = 0

        configFileName = f"{Game.__getPathGame()}/{Constantes.CONFIG_FILE}"

        # if os.path.exists(configFileName):
        Config.loadConfig(configFileName)

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
        playerIniciaRonda = self.players[self.lastTurnIndex]

        for numRonda in range(self.lastRound + 1, Config.max_rondas + 1):
            # Empieza la ronda
            frase = Phrase.getPhrase()
            ronda = RoundGame(numRonda, self.players, frase, playerIniciaRonda)
            playerIniciaRonda = ronda.playRound()

            # Ronda finalizada --> Guarda la partida
            self.__saveGame()

    def __endGame(self):
        """
        Encargado de finalizar el juego
        :return:
        """
        # MOSTRAR EL GANADOR

    @staticmethod
    def __getPathGame():
        return f"{os.path.expanduser('~')}/{Constantes.FOLDER_ROOT}"

    @staticmethod
    def __checkFolderGame():

        userPathHome = os.path.expanduser('~')
        pathDirGame = f"{userPathHome}/{Constantes.FOLDER_ROOT}"
        if not os.path.isdir(pathDirGame):
            # Crear el directorio
            os.mkdir(pathDirGame)

        return

    def __loadGame(self):
        """
        Este metodo...
        :return: True si existe partida guarda, y por tanto el juego se configura en base a esta partida. False en caso contrario
        """

        # 1. Verificar si existe ruta, y dentro de la ruta existe un fichero. SINO SALIR FALSO
        Game.__checkFolderGame()

        filename = f"{Game.__getPathGame()}/{self.config.partida_formato}"

        if os.path.isfile(f"{filename}.csv"):
            return self.__loadGameCSV(f"{filename}.csv")

        if os.path.isfile(f"{filename}.json"):
            return self.__loadGameJson(f"{filename}.json")

        return False

    def __loadGameCSV(self, filename):
        """

        :return:
        """

        # 1. Revivar si existe un fichero en la ruta y del tipo adecuado (CSV)

        # 2. Llamar Lector CSVReader del módulo de Python. Obtener información de las columnas
        self.players.clear()

        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                line_count += 1
                if line_count == 1:
                    self.lastRound = int(row["ultima_ronda"])
                    self.lastTurnIndex = int(row["ultimo_jugador_turno"])

                # 2. -> Construir los players, construir la ronda, ronda_actual
                tipoEnum = TipoJugadorEnum(int(row["jugador-tipo"]))
                player = Player.FromSavedPlayer(row["jugador-nombre"], int(row["jugador-dinero-total"]), tipoEnum)
                self.players.append(player)

        return True

    def __loadGameJson(self, filename):

        filepartida = f"{Game.__getPathGame()}/{Constantes.PARTIDA_SAVE_FILENAME}.{Config.partida_formato}"

        if not os.path.exists(filepartida):
            return False

        partida_data = {}
        with open(filepartida, 'r') as json_file:
            partida_data = json.load(json_file)

        # Pasar de la información en formato diccionario a las variables del programa
        self.lastRound = int(partida_data["ultima_ronda"])
        self.lastTurnIndex = int(partida_data["ultimo_jugador_turno"])

        # Iterar por todos los jugadores o elemtos que haya en el Array de Jugadores
        for pdict in partida_data["jugadores"]:
            tipoEnum = TipoJugadorEnum(int(pdict["jugador-tipo"]))
            player = Player.FromSavedPlayer(pdict["jugador-nombre"], int(pdict["jugador-dinero-total"]),
                                            tipoEnum)
            self.players.append(player)

        return True

    def __saveGame(self):

        if Config.partida_formato == "json":
            return self.__saveGameJson()

        if Config.partida_formato == "csv":
            return self.__saveGameCSV()

        raise Exception("Formato guardado no reconocido")

    def __saveGameJson(self):

        data = {
            "ultimo_jugador_turno": self.lastTurnIndex,
            "ultima_ronda": self.lastRound,
            "jugadores": []
        }

        for player in self.players:
            player_dict = {
                "jugador-tipo": player.tipo.value,
                "jugador-nombre": player.name,
                "jugador-dinero-total": player.prizeMoney
            }
            data["jugadores"].append(player_dict)

        filepartida = f"{Game.__getPathGame()}/{Config.partida_formato}.{Constantes.PARTIDA_SAVE_FORMATO}"

        with open(filepartida, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def __saveGameCSV(self):
        pass
