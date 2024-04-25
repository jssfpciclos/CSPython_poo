# archivo main donde se inicia el juego
from juego_ruleta import Game, HumanPlayer, RoundGame, Phrase, Config
from juego_ruleta import DatabaseUtils


def create_fichero_partida_csv():
    pass


def startGame():
    game = Game()
    game.start()


def testBuildPlayers(numPlayers: int = 2):
    if numPlayers is 2:
        return [HumanPlayer("Angel"), HumanPlayer("Ramon")]

    if numPlayers is 3:
        return [HumanPlayer("Angel"), HumanPlayer("Ramon"), HumanPlayer("Manuel")]

    raise Exception("Número de jugadores no contralado")


def testRound():
    players = [HumanPlayer("Angel"), HumanPlayer("Ramon")]
    frase = Phrase("frases celebres", "La vida es sueño", "Filosofía")
    round = RoundGame(1, players, frase, players[0])

    round.playRound()


def testRoundTurn():
    players = [HumanPlayer("Angel"), HumanPlayer("Ramon")]
    frase = Phrase("frases celebres", "La vida es sueño", "Filosofía")
    round = RoundGame(1, players, frase, players[0])

    round._RoundGame__playTurn(players[0])


def test_ObscucerFrase():
    players = [HumanPlayer("Angel"), HumanPlayer("Ramon")]
    panel = Phrase("frases celebres", "El bueno, el feo y el malo", "Filosofía")
    round = RoundGame(1, players, panel, players[0])

    # round.__oscurecerFrase(frase, ["f","s","b"])
    frase_obscurecida = round._RoundGame__oscurecerFrase(panel.frase, ["B", "N", "T", "Q"])
    print(frase_obscurecida)


def testInitGame():
    playerSimulated = testBuildPlayers(numPlayers=2)
    game = Game(players=playerSimulated)
    game.start()
    print(game.players)


def testLoadGame():
    game = Game()
    game._Game__loadGame()


def testSaveGame():
    playerSimulated = testBuildPlayers(numPlayers=2)
    game = Game(players=playerSimulated)
    game._Game__saveGame()


def testConfigLoad():
    Config.loadConfig(f"{Game._Game__getPathGame()}/config.yml")
    print(Config.partida_formato)
    print(Config.max_rondas)


class TestDatabase:

    @staticmethod
    def init():
        DatabaseUtils.init_db()
        Phrase._Phrase__check_copy_phrases_to_database()
        fr = Phrase.getPhrase("refranes")
        print(fr)




if __name__ == '__main__':
    TestDatabase.init()
    startGame()
    testConfigLoad()
    # testInitGame()
    # testRound()
    # testLoadGame()
    # testRoundTurn()
    # test_ObscucerFrase()
    # testSaveGame()
