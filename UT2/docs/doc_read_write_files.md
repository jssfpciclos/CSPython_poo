# UT2. Leer y escribir ficheros en Python

## 1. Introducción

En esta unidad vamos a ver cómo trabajar con ficheros en Python. Para ello, vamos a ver cómo abrir un fichero, leerlo, escribir en él, etc.


## 2. Lectura de un fichero

Python ofrece la función `open()` para abrir un fichero. Esta función devuelve un objeto de tipo fichero que podemos utilizar para leer o escribir en el fichero. Esta apertura se puede realizar de 3 modos:

 - **Lectura** del contenido de un fichero existente.
 - **Escritura** del contenido en un fichero nuevo.
 - **Añadir** contenido de un fichero existente.

Veamos un ejemplo para leer el contenido de un fichero en el que se encuentran las temperaturas mínimas y máximas de cada día de la última semana. El fichero está en la subcarpeta (ruta relativa) files/temps.dat y tiene el siguiente contenido:

```data
23 29
23 31
26 34
23 33
22 29
22 28
22 28
```

El código para leer el fichero es el siguiente:

```python
fichero = open("files/temps.dat", "r")
```

La función `open()` recibe como primer argumento la ruta al fichero que queremos manejar (como un «string») y como segundo argumento el modo de apertura (también como un «string»). Nos devuelve el manejador del fichero, que en este caso lo estamos asignando a una variable llamada `f` pero le podríamos haber puesto cualquier otro nombre.

> 💡 **Nota**<br>
> Es importante dominar los conceptos de ruta relativa y ruta absoluta para el trabajo con ficheros. Véase este artículo de DeNovatoANovato.com: [Rutas relativas y absolutas en Python](https://www.denovatoanovato.com/diferencia-entre-ruta-absoluta-y-ruta-relativa-en-python/).


El manejador del fichero se implementa mediante un *flujo de entrada/salida* para las operaciones de lectura/escritura. Este objeto almacena, entre otras cosas, la ruta al fichero, el modo de apertura y la codificación:

```python
>>> f
<_io.TextIOWrapper name='files/temps.dat' mode='r' encoding='UTF-8'>
```

> ➡️ **Truco**<br>
> Existen muchas [codificaciones de caracteres](https://es.wikipedia.org/wiki/Codificaci%C3%B3n_de_caracteres) para ficheros, pero la más utilizada es [UTF-8](https://es.wikipedia.org/wiki/UTF-8) ya que es capaz de representar cualquier caracter [Unicode](https://unicode-table.com/en/blocks/) al utilizar una longitud variable de 1 a 4 bytes..


Hay que tener en cuenta que la ruta al fichero que abrimos (en modo lectura) debe existir, ya que de lo contrario obtendremos un error:

```python
>>> f = open('foo.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'foo.txt'
```
Una vez abierto el fichero ya podemos proceder a leer su contenido. Para ello Python nos ofrece la posibilidad de leer todo el fichero de una vez o bien leerlo línea a línea.

### 2.1. Lectura de todo el fichero

Siguiendo con nuestro ejemplo de temperaturas, veamos cómo leer todo el contenido del fichero de una sola vez. Para esta operación, Python nos provee, al menos, de dos funciones:

- **read()**: Devuelve todo el contenido del fichero como una cadena de texto (str):

  ```python
  >>> # Podemos obviar 'r' ya que es el modo por defecto!
  >>> f = open('files/temps.dat')

  >>> f.read()
  >>> '23 29\n23 31\n26 34\n23 33\n22 29\n22 28\n22 28\n'
  ```
- **readlines()**: Devuelve todo el contenido del fichero como una lista (list) donde cada elemento es una línea:
  
  ```python
  >>> f = open('files/temps.dat')

  >>> f.readlines()
  ['23 29\n', '23 31\n', '26 34\n', '23 33\n', '22 29\n', '22 28\n', '22 28\n']
  ```

> 🔥 **Importante**<br>
> Nótese que, en ambos casos, los saltos de línea \n siguen apareciendo en los datos leídos, por lo que habría que «limpiar» estos caracteres, utilizando las funciones de las cadenas de texto, como por ejemplo `strip()` o `replace()`.

### 2.2. Lectura línea a línea

Hay situaciones en las que interesa leer el contenido del fichero línea a línea. Imaginemos un fichero de tamaño considerable (varios GB). Si intentamos leer completamente este fichero de sola una vez podríamos ocupar demasiada RAM y reducir el rendimiento de nuestra máquina.

Es por ello que Python nos ofrece varias aproximaciones a la lectura de ficheros línea a línea. La más usada es iterar sobre el propio manejador del fichero, ya que los ficheros son estructuras de datos iterables:

```python
>>> f = open('files/temps.dat')

>>> for linea in f:
...     print(linea)
...
23 29

23 31

26 34

23 33

22 29

22 28

22 28
```

#### Lectura de una línea

Hay ocasiones en las que nos interesa leer únicamente una sola línea. Es cierto que esto se puede conseguir mediante la aproximación anterior. Sería algo como:

```python
>>> f = open('files/temps.dat')

>>> for linea in f:
...     print(linea)
...     break
...
23 29
```
Pero Python también ofrece la función readline() que nos devuelve la siguiente línea del fichero:

```python
>>> f = open('files/temps.dat')

>>> f.readline()
'23 29\n'
```

Es importante señalar que cuando utilizamos la función readline() el «puntero de lectura» se desplaza a la siguiente línea del fichero, con lo que podemos seguir cargando la información según nos interese:

```python
>>> f = open('files/temps.dat')

>>> f.readline()
'23 29\n'

>>> f.readline()
'23 31\n'

>>> f.readline()
'26 34\n'
``` 

**Los ficheros se agotan**

Hay que tener en cuenta que, una vez abierto el fichero, la lectura de su contenido se puede realizar una única vez. O dicho de otra manera, el iterable que lleva implícito «se agota».

Veamos este escenario con el ejemplo anterior:

```python
>>> f = open('files/temps.dat')

>>> for linea in f:
...     print(line.strip(), end=' ')
...
23 29 23 31 26 34 23 33 22 29 22 28 22 28

>>> for linea in f:
...     print(line.strip(), end=' ')
...  # No se imprime nada! --> El fichero se ha agotado
``` 

Esto mismo ocurre si utilizamos funciones como read() o readlines().

> 🚧 **Advertiencia**<br>
> Por este motivo y también por cuestiones de legibilidad del código, deberíamos abrir un fichero una única vez y realizar todas las operaciones de lectura necesarias, siempre que las circunstancias lo permitan.


## 3. Escritura en un fichero

Para escribir texto en un fichero hay que abrir dicho fichero en modo escritura. Para ello utilizamos el argumento adicional en la función open() que indica esta operación:

```python
>>> f = open('files/canary-iata.dat', 'w')
```

> 💡 **Nota**<br>
> Si bien el fichero en sí mismo se crea al abrirlo en modo escritura, la ruta hasta ese fichero no. Eso quiere decir que debemos asegurarnos que las carpetas hasta llegar a dicho fichero existen. En otro caso obtenemos un error de tipo FileNotFoundError.

Ahora ya podemos hacer uso de la función `write()` para enviar contenido al fichero abierto.

Supongamos que queremos volcar el contenido de una lista/tupla en dicho fichero. En este caso partimos de los códigos IATA de aeropuertos de las Islas Canarias.

```python
>>> aeropuertos = ('GMZ', 'VDE', 'SPC', 'TFN', 'TFS')

>>> for code in aeropuertos:
...     f.write(code + '\n')  # Añadimos el salto de línea, ya que no lo incluye por defecto
...

>>> f.close()   # Cerrar el fichero es fundamental para eviar perdida de datos, especialmente en modo escritura!
```

> 🚧 **Advertencia**<br>
> Siempre que se abre un fichero en modo escritura utilizando el argumento 'w', el fichero se inicializa, borrando cualquier contenido que pudiera tener.

Otra forma de escribir la tupla «de una sola vez» podría ser utilizando la función join() con el salto de línea como separador:

```python
>>> f = open('files/canary-iata.dat', 'w')

>>> f.write('\n'.join(aeropuertos))

>>> f.close()
```

En el caso de que ya tengamos una lista (iterable) cuyos elementos tengan el formato de salida que necesitamos (incluyendo salto de línea si así fuera necesario) podemos utilizar la función writelines() que nos ofrece Python.

Siguiendo con el ejemplo anterior, imaginemos un escenario en el que la tupla ya contiene los saltos de línea:

```python
>>> aeropuertos = ('GMZ\n', 'VDE\n', 'SPC\n', 'TFN\n', 'TFS\n')

>>> f = open('files/canary-iata.dat', 'w')
>>> f.writelines(aeropuertos)
>>> f.close()
```

### 3.1. Añadir contenido a un fichero

La única diferencia entre añadir información a un fichero y escribir información en un fichero es el modo de apertura del fichero. En este caso utilizamos 'a' por «append»:

```python
>>> f = open('files/canary-iata.dat', 'a')
>>> f.write('LPA\n')
>>> f.close()
```

En este caso el fichero no se inicializa, sino que se añade el contenido al final del fichero.

### 3.2 Usando contextos

Python ofrece [gestores de contexto](./doc_gestores_contexto.md) como una solución para establecer reglas de entrada y salida a un determinado bloque de código.

En el caso que nos ocupa, usaremos la sentencia with y el contexto creado se ocupará de cerrar adecuadamente el fichero que hemos abierto, liberando así sus recursos:

```python
# El fichero se abre en modo lecutra utilizando el gestor de contexto definido por la palabra reservada 'with'
with open('files/temps.dat') as f:
    # Lectura del fichero línea a línea utilizando la iteración sobre el manejador del fichero.
    for line in f:
        # Limpieza de saltos de línea con strip() encadenando la función split() para separar las dos temperaturas por el carácter espacio.
        min_temp, max_temp = line.strip().split()
        print(min_temp, max_temp)

23 29
23 31
26 34
23 33
22 29
22 28
22 28
```

Hay que prestar atención a la hora de escribir valores numéricos en un fichero, ya que el método write() por defecto espera ver un «string» como argumento:

```python
>>> lottery = [43, 21, 99, 18, 37, 99]

>>> with open('files/lottery.dat', 'w') as f:
...    for number in lottery:
...        f.write(number + '\n')
...

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: write() argument must be str, not int
```

Para solucionar este problema podemos utilizar la función str() para convertir el número en un «string»:

```python
>>> lottery = [43, 21, 99, 18, 37, 99]

>>> with open('files/lottery.dat', 'w') as f:
...    for number in lottery:
...        f.write(str(number) + '\n')
...
```


