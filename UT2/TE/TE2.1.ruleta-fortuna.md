# Tarea Evaluable 2.1. Ruleta de la Fortuna

## Enunciado

El programa debe simular una versión simplificada del juego de la "ruleta de la fortuna". 

- Los jugaddores pueden ser personas, o el ordenador puede ser otro jugador.<br>
  _Cada jugador tiene una cantidad de dinero inicial (0€) que va aumentando o disminuyendo en función de los premios obtenidos_.

- El objetivo es adivinar una frase oculta, dentro de una categoria. Por ejemplo, "películas", "refranes", etc, con una pista.
- El jugador observa la frase a través de una serie de guiones que representan las letras de la frase. Cada letra está representada por un guión bajo. Por ejemplo, la frase "Hola mundo" se representaría como "_ _ _ _ _   _ _ _ _ _ _".
- Durante su turno, cada jugador gira una ruleta para determinar el premio que obtiene. 
  - La ruleta tiene 24 casillas, cada una con un premio asociado.
  - Los premios pueden ser positivos o negativos.

Durante una tirada del jugador, pueden ocurrir las siguientes situaciones:

1. Si la ruleta se detiene en una casilla con dinero, puede hacer una de las siguientes acciones:
   - `Elegir una Vocal` (no elegida ya). La vocal cuesta (250€), si no tiene suficiente dinero, no puede elegir una vocal. `Elegir una consonante` de la frase (no elegida ya), no tiene coste.
   - Si la letra está en la frase:
     - Obtiene una recompensa por cada ocurrencia de la letra en la frase, por ejemplo, si la letra elegida es "a", la casilla tenía un premio de 100€ y la frase es "Hola mundo", el premio sería 200€. El jugador mantiene su turno, si no pasa el turno al siguiente jugador.
     - Si no, el premio es 0 y pasa el turno al siguiente jugador.
  
  - Adivinar la frase completa, escribiendo la frase.
    - Si la frase es correcta, el jugador gana el premio acumulado.
    - Si la frase es incorrecta, el premio es 0 y pasa el turno al siguiente jugador.

  - Pasar el turno al siguiente jugador, diciendo "Paso"
  

   - Adivinar una consonante de la frase (no elegida ya). Si la letra está en la frase, el jugador recibe el premio de la ruleta. Si no está, el premio es 0.


2. Si la ruleta se detiene en una casilla "Pierde Turno", el jugador pierde el turno y el juego pasa al siguiente jugador.

3. Si la ruleta se detiene en una casilla "Quiebra", el jugador pierde todo su dinero de esta partida, pero mantiene todo el dinero que haya ganado en partidas anteriores.




## Especificaciones

### Clase `Game`

Clase más importante del juego. 

Constantes:

- TOTAL_ROUNDS: Número de rondas que se jugarán en el juego.
- VOCAL_PRECIO: Precio de la vocal (250€)
- RECOMPENSA_PANEL: Premio por resolver el panel (500€)
- Resto de constantes que consideres necesarias.


Pasos:

1. Inicio del juego
   - Mostrar bienvenida
   - Preguntar el número de jugadores y sus nombres
  
2. Se juegan tantas rondas/paneles como se haya indicado en la constante TOTAL_ROUNDS.
   - Cada ronda se juega con un panel distinto.
   - Al final de cada ronda, se muestra el dinero acumulado de cada jugador.

3. Una vez finalizadas todas las rondas, se muestra el ganador del juego.


### Player

Debes crear una clase `Player` (abstracta) que represente a un jugador. La clase debe tener los siguientes atributos de instancia:

Atributos:

- `name`: Nombre del jugador (Constructor)
- `prizeMoney`: Dinero acumulado por el jugador
- `prizeMoneyRound`: Dinero acumulado en la ronda actual

Métodos:

- `addMoney(amt)`: Añade dinero (int) dinero al premio acumulado
- `applyBankrupt()`: Establece el premio acumulado a 0 (Qiebra)
- `addPrizeRound(prize)`: Añade el premio a la ronda actual
- `applyWinRound()`: Añade el premio de la ronda actual (sumando la recompensa del panel) al premio acumulado
- `goMove()`: Método abstracto que debe ser implementado por las clases hijas. Devuelve el resultado de la tirada del jugador, junto con el premio obtenido.
- Al imprimir el objeto, debe mostrar el nombre del jugador y el premio acumulado.  `Ramón: 1000€`

### Clase HumanPlayer

Debes crear una clase `HumanPlayer` que herede de `Player`. Además de tener los atributos y métodos de `Player`, debe tener los siguientes métodos:

Métodos:

- `goMove()`: Implementa el método.


### Clase ComputerPlayer

(por definir)

### Clase Ruleta

Representa la ruleta del juego, los valores son los premios que se pueden obtener.

Los valores son los siguientes: 
```python
[100, 50, 100, 150, 50, 200, 250, 50, 100, 150, 300, -1, 400, 0, 500, 200, 100, 50, 250, 150, 100, 50, 200]
```	
Métodos:

- `girar()`: Devuelve un valor aleatorio de la ruleta.

Valores:

- -1: Quiebra o Bancarrota
-  0: Pierde Turno
-  Resto_valores: Premio obtenido

### Clase RoundGame

Representa una ronda del juego, concretamente la resolución de un panel.

En cada ronda, se tiene que elegir una nueva frase, con una categoria.

Cuando se finaliza la ronda, puede finalizar con dos resultados:

- Salir del juego: El jugador/es ha decidido salir del juego.
- Ganar la ronda: Uno de los jugadores ha resuelto el panel.

Métodos:

- `playRound()`: Método que se encarga de jugar una ronda. 
  - Comienza el jugador siguiente al que ha ganado la ronda anterior
  - Las opciones de un jugador son:
    - Girar la ruleta (obtener premio, bancarrota, pierde turno)
    - Elegir una vocal (si tiene dinero acumulado en la ronda) o consonante
    - Indicar una letra o resolver el panel
    - Pasar el turno
  
  - Si no se resuelve el panel, el juego pasa al siguiente jugador. 
  - Se repiten los pasos anteriores hasta que el panel se resuelva el panel o se decida salir.