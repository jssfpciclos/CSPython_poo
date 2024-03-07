# archivo main donde se inicia el juego
from juego_ruleta import Game, HumanPlayer


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


def testInitGame():
    playerSimulated = testBuildPlayers(numPlayers=2)
    game = Game(players=playerSimulated)
    game.start()
    print(game.players)


if __name__ == '__main__':
    # startGame()
    testInitGame()
