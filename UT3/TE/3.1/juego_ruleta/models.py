from peewee import *
from .database import *


class PlayerModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    alias = CharField(max_length=50, unique=True)

    class Meta:
        database = metricaDB
        table_name = 'jugador'


class GameModel(Model):
    id = AutoField(primary_key=True)
    startDate = DateTimeField()
    endDate = DateTimeField(null=True)
    winnerPrice = IntegerField(default=0)

    class Meta:
        database = metricaDB
        table_name = 'partida'


class GamePlayerModel(Model):
    player = ForeignKeyField(PlayerModel, backref='games')
    game = ForeignKeyField(GameModel, backref='players')
    playerGamePrize = IntegerField(default=0)

    class Meta:
        database = metricaDB
        table_name = 'JugadorPartida'


class PhraseModel(Model):
    id = AutoField(primary_key=True)
    category = CharField(max_length=50)
    pista = CharField(max_length=50)
    frase = CharField(max_length=500)

    class Meta:
        database = metricaDB
        table_name = 'frase'


class RoundModel(Model):
    id = AutoField(primary_key=True)
    code = CharField(max_length=5, unique=True)  # 10.1
    number = IntegerField()  # 1
    winnerPrize = IntegerField(default=0)

    game = ForeignKeyField(GameModel, backref='rounds')
    frase = ForeignKeyField(PhraseModel, backref='rounds')

    class Meta:
        database = metricaDB
        table_name = 'ronda'


class DatabaseUtils:

    @staticmethod
    def init_db():
        metricaDB.connect()
        metricaDB.create_tables([PlayerModel, GameModel, GamePlayerModel, PhraseModel, RoundModel])
