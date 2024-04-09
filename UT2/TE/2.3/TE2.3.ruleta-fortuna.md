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
class Config:
    MAX_ROUND = 10
    PARTIDA_FORMATO = 'CSV'
    VOCAL_PRECIO = 100
    RECOMPENSA_PANEL = 500
    MAX_PLAYER_NUMBER = 3


  # Cargar la configuración desde el fichero de configuración
  @staticmethod
  Config.loadConfig(cls):
    # modificar las propiedades de la clase con los valores del fichero de configuración
    pass
```

> **Nota**
> Dentro del juego, será necesario cambiar las referencias a las constantes por las propiedades de la clase `Config`.
