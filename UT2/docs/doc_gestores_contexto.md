# Gestores de contexto

Otra de las aplicaciones interesantes de los métodos mágicos/especiales es la de los *gestores de contexto*. Un gestor de contexto permite aplicar una serie de acciones a la entrada y a la salida del bloque de código que engloba.

Hay dos métodos que son utilizados para implementar los gestores de contexto:

- __enter__() Acciones que se llevan a cabo al entrar al contexto.

- __exit__() Acciones que se llevan a cabo al salir del contexto.


Veamos un ejemplo en el que implementamos un gestor de contexto que mide tiempos de ejecución:

```python
import time

class Timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start) * 1000
        print(self.message.format(elapsed_time))
```

Aunque en este caso no estamos haciendo uso de los parámetros en la función __exit__(), hacen referencia a una posible excepción (error) que se produzca en la ejecución del bloque de código que engloba el contexto. Los tres parámetros son:

- `exc_type` indicando el tipo de la excepción.
- `exc_value` indicando el valor (mensaje) de la excepción.
- `exc_traceback` indicando la «traza» (pila) de llamadas que llevaron hasta la excepción.

Ahora podemos probar nuestro gestor de contexto con un ejemplo concreto. La forma de «activar» el contexto es usar la sentencia with seguida del símbolo que lo gestiona:

```python
with Timer("Elapsed time: {} ms"):
    time.sleep(1)
```

Otro ejemplo:

```python
with Timer():
    for _ in range(1_000_000):
        x = 2 ** 20
# Execution time (seconds): 0.05283

with Timer():
    x = 0
    for _ in range(1_000_000):
        x += 2 ** 20
# Execution time (seconds): 0.08749
```

Ahora vamos a ver un ejemplo más complejo en el que se utiliza un gestor de contexto para abrir un fichero y escribir en él:

```python
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, type, value, traceback):
        self.open_file.close()

with File('test.txt', 'w') as f:
    f.write('Hola\n')
    f.write('Adiós\n')
```

La ventaja que tiene utilizar gestores de contexto, es que nos aseguramos que el fichero se cierra correctamente, incluso si se produce una excepción en el bloque de código que engloba el contexto.

```python	
try:
    with File('test.txt', 'w') as f:
        f.write('Hola\n')
        f.write('Adiós\n')
except ZeroDivisionError:
    # Al lanzar una excepción, el método __exit__() se ejecuta, ya la variable `f` pierde el ámbito, y se destruye.
    print('Error: No se puede dividir por cero')
```

