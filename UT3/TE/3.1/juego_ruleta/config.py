import os.path

import yaml

from .constantes import Constantes


class Config:
    max_player_number = 3
    max_rondas = Constantes.TOTAL_ROUNDS
    vocal_precio = Constantes.VOCAL_PRECIO
    recompensa_panel = Constantes.RECOMPENSA_PANEL
    partida_formato = Constantes.PARTIDA_SAVE_FORMATO

    @staticmethod
    def loadConfig(filename):
        # modificar las propiedades de la clase con los valores del fichero de configuración

        # si fichero existe, sino nada
        if os.path.exists(filename):

            with open(filename, 'r') as file:
                config = yaml.load(file, Loader=yaml.FullLoader)

                Config.max_player_number = Config.__getValue(config, "general.maximo_jugadores",
                                                             defaultValue=3)
                Config.max_rondas = Config.__getValue(config, "general.maximo_rondas",
                                                      defaultValue=Constantes.TOTAL_ROUNDS)
                Config.vocal_precio = Config.__getValue(config, "premios.vocal_precio",
                                                        defaultValue=Constantes.VOCAL_PRECIO)

                Config.recompensa_panel = Config.__getValue(config, "premios.recompensa_panel",
                                                            defaultValue=Constantes.RECOMPENSA_PANEL)

                Config.partida_formato = Config.__getValue(config, "formato.tipo",
                                                           defaultValue=Constantes.PARTIDA_SAVE_FORMATO)

        else:
            Config.saveConfig(filename)


    @staticmethod
    def saveConfig(filename):

        # Crear la estructura en formato Json
        data = {
            "general": {
                "maximo_rondas": Config.max_rondas,
                "maximo_jugadores": Config.max_player_number
            },
            "formato": {
                "tipo": Config.partida_formato
            },
            "premios": {
                "vocal_precio": Config.vocal_precio,
                "recompensa_panel": Config.recompensa_panel
            }
        }

        with open(filename, 'w') as file:
            yaml.dump(data, file)


    @staticmethod
    def __getValue(values, key, defaultValue):

        keys = key.split('.')
        if len(keys) == 1:
            return values.get(key, defaultValue)

        valor_anterior = values
        for k in keys:
            valor_anterior = valor_anterior.get(k)
            if valor_anterior is None:
                return defaultValue

        return valor_anterior
