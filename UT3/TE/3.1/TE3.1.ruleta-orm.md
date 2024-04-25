# Tarea Evaluable 3.1. Ruleta de la Fortuna. Gestión de Base de Datos

Siguiendo con el desarrollo del juego, y para mejorarlo se desea guardar la información de las partidas, jugadores y premios en una base de datos, para así poder obtener estadísticas y conocer por ejemplo, el jugador que más partidas ha ganado, el premio más alto entregado, las partidas más largas, etc.

Para ello se va a utilizar una BD SQLite, y se va a utilizar el ORM Peewee para gestionar la base de datos.

## Enunciado

Se requieren guardar la siguiente información del juego:

- Jugadores
- Partidas
- Rondas (de cada partida)
- Frases (banco de frases)

Para esto se requiere modelar las tablas necesarias y crear las relaciones entre ellas, con el fin de poder obtener toda la información que se requiere.


## Modelo de datos

El modelo de datos a implementar es el siguiente:

**Modelo PlayerModel**

Datos que se requieren de un jugador:

- Nombre
- Nick  (El nick debe ser único)

- Partidas (Relación con el modelo Partida) 

**Modelo GameModel**

Una partida se debe almacenar la siguiente información:

- FechaInicio (Fecha y hora)
- FechaFin (Fecha y hora)
- PremioTotalGanador
- Ganador (Relación con el modelo Jugador)
- Rondas (Relación con el modelo Ronda)
- Jugadores (Relación con el modelo Jugador)


**Modelo GamePlayerModel**

Donde se almacena la relación entre la partida y los jugadores que han participado en ella.

Además de la relación, se debe guardar el dinero que ha ganado cada jugador en la partida.

- Partida (Relación con el modelo Partida)
- Player (Relación con el modelo Jugador)

**Modelo Ronda**

Una ronda se debe almacenar la siguiente información:

- Numero (Es el número de ronda dentro de la partida)
- PremioGanador (Es el premio que ha ganado el ganador de la ronda)
- Ganador (Relación con el modelo Jugador)
- Frase (Relación con el modelo Frase)
- Partida (Relación con el modelo Partida)

**Modelo Frase**

En este modelo se deben almacenar las frases que se van a utilizar en el juego.

- Categoria
- Pista
- frase



### Objetivos

- Aplicar los conceptos de ORM aprendidos en el curso a un caso práctico.
- Conocer el objetivo y utilidad de los ORM.
- Conocer como modelar una base de datos relacional.

## Tarea a desarrollar

### Crear modelo E/R

Crear el modelo de E/R de la BD, indicando las tablas, campos y relaciones entre ellas.


### Crear los modelos

Utilizando el ORM Peewee, crear los modelos necesarios para gestionar la base de datos.

Los modelos deben estar en un fichero llamado `models.py` y deben estar en el paquete `ruleta_fortuna`.

### Crear la base de datos

Crear un fichero llamado `database.py` en el paquete `ruleta_fortuna`, que se encargue de las siguientes acciones:

- Inicializar la base de datos
- Acciones relacionadas con la base de datos (genéricas)

Crear también una clase `Database` con los métodos estáticos:

- `init_db()`: Inicializa la base de datos.


### Incluir funcionalidad en el Juego

**Frase**

Ahora las frases deben ser seleccionadas desde la BD, por tanto desde la Entidad `Frase` se debe modificar el comportamiento para que obtenga una frase aleatoria de la BD.
Ahora la frase debe convertirse en un modelo de la base de datos.

Una posible implementación podría ser esta:

```python
class Frase(Model):
    id = IntegerField(primary_key=True)
    categoria = CharField(max_length=255)
    pista = CharField(max_length=255)
    texto = CharField(max_length=255)

    class Meta:
        database = db

    @staticmethod
    def get_random():
        return Frase.select().order_by(fn.Random()).get()
```

**Partida**

Cada vez que se inicie una nueva partida, se debe guardar la información de la misma. Para ello la clase `Game` debe hacer uso del modelo `PartidaModel` para guardar la información de la partida.

Cada vez que se finalize la partida, hay que actualizar los valores de la misma, ganador, fecha fin, premio total, etc.


**Ronda**

Cada vez que se inicie una nueva ronda, al igual que la partida, también se debe crear el registro de la misma en BD, y actualizar los valores de la ronda al finalizar.

Para ello, seguimos el mismo procedimiento que con la partida, pero utilizando el modelo `RondaModel`.

> 💡 Recordar que también hay que indicar el ganador de la misma.

**Jugadores**

... pendiente de definir
