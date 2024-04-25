
class Constantes:
    TOTAL_ROUNDS = 3
    CONSONANTES = set("BCDFGHJKLMNÑPQRSTVWXYZ")  # Conjunto de consonantes
    VOCALES = set("AEIOU")  # Conjunto de vocales
    ABECEDARIO = CONSONANTES.union(VOCALES)  # C
    SIGNOS = set(" ,¿?!¡")
    VOCAL_PRECIO = 250
    RECOMPENSA_PANEL = 500

    FOLDER_ROOT = ".ruleta_fortuna"
    PARTIDA_SAVE_FILENAME = "savedgame"
    PARTIDA_SAVE_FORMATO = "json"
    CONFIG_FILE = "config.yml"

    DATABASE_NAME = "metricas.db"