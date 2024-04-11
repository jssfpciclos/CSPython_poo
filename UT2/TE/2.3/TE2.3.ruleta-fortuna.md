# Tarea Evaluable 2.3. Ruleta de la Fortuna. Fichero configuración

Siguiendo con el desarrollo de la tarea evaluable 2.2, se pide añadir la funcionalidad de crear un fichero de configuración para el juego, en formato YAML.
El fichero de configuración si existe, estará almacenado en la carpeta `.ruleta_fortuna` en el home del usuario.

## Enunciado

El juego necesita una configuración inicial, que ahora mismo se está guardando en `constantes` o directamente en datos `hardcode` (puestos directamente en el código).
El problema de esta opción, es que ante cualquier cambio necesitamos modificar el código, y no es lo más adecuado.

Para ello son muy útiles los ficheros de configuración, que nos permiten modificar la configuración del programa sin tener que modificar el código fuente.

## Especificaciones

- El fichero de configuración se debe guardar en la carpeta `.ruleta_fortuna` en el home del usuario.
- El nombre del fichero de configuración es `config.yaml`.
- El fichero de configuración debe contener la siguiente información:
  - MAX_ROUND: Número máximo de rondas.
  - PARTIDA_FORMATO: Formato de guardado de la partida. (CSV o JSON)
  - VOCAL_PRECIO: Precio de la vocal.
  - RECOMPENSA_PANEL: Recompensa por acertar el panel.
  - MAX_PLAYER_NUMBER: Número máximo de jugadores.

En caso de que un parámetro no exista en el fichero de configuración, se debe usar el valor por defecto contennido en el valor del fichero de constantes.

### Objetivos

- Aplicar los conceptos de manejor de ficheros aprendidos en el curso a un caso práctico.
- Conocer el objetivo y utilidad de los ficheros de configuración.
- Conocer como cargar información de ficheros de configuración y su integración en un programa
- Aplicar trabajo con ficheros en formato YAML.

## Tareaa a desarrollar

Integrar la carga de la configuración del juego desde un fichero de configuración en formato YAML.

Para la integración del fichero de configuración, se va a crear una clase `Config` que se encargará de cargar la configuración del juego desde el fichero de configuración, y tendrá una propiedad para cada parámetro de configuración.

Esta clase será estática, y se cargará la configuración en el momento de importar el módulo.

```python
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

        
        if os.path.exists(filename):
            # Si el fichero existe, se carga con los valores contenidos dentro del fichero
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
            # Si el fichero no existe, se crea con la configuración de las variables de la clase
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
```

> **Nota**
> Dentro del juego, será necesario cambiar las referencias a las constantes por las propiedades de la clase `Config`.
