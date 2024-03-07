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

Los modos más comunes de apertura de ficheros son:

- **r**: Lectura (por defecto).
- **w**: Abierto para escritura, eliminando el contenido.
- **a**: Abierto para escritura, añadiendo contendo al final si el fichero existe.
- **b**: Modo binario.
- **+**: Modo lectura/escritura.

También existen combinaciones de estos modos, como por ejemplo 'rb' para lectura en modo binario o 'r+' para lectura/escritura. 

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


### 3.3. Categorias de ficheros

Los ficheros se pueden clasificar en dos categorías:

- **Ficheros de texto**: Contienen texto legible para el ser humano. Son ficheros que se pueden abrir con un editor de texto y leer su contenido. Los ficheros de texto pueden contener cualquier tipo de datos, como números, letras, símbolos, etc.
- **Ficheros binarios**: Contienen datos que no están en un formato legible para el ser humano. Son ficheros que no se pueden abrir con un editor de texto y leer su contenido. Los ficheros binarios pueden contener cualquier tipo de datos, como imágenes, sonidos, vídeos, etc.
- **Buffered Binary Files**: Son ficheros binarios que se leen o escriben en bloques de datos. Son más rápidos que los ficheros binarios normales, ya que se leen o escriben en bloques de datos en lugar de leer o escribir byte a byte.

Cada unos de estas categorias son definidos en el módulo `io` de Python. Por ejemplo, para abrir un fichero en modo lectura de texto:

#### 3.3.1. Ficheros de texto

```python
open('file.txt', 'r')
open('file.txt', 'rt')
open('file.txt', 'w')
```

Todos estos tipos de ficheros, devuelven un objeto de tipo `TextIOWrapper`: 

```python
>>> f = open('files/temps.dat', 'r')
>>> type(f)
<class '_io.TextIOWrapper'>
```

Es el ojbeto por defecto retornado por la función `open()`.

#### 3.3.2. Buffered Ficheros binarios

Un Buffered Binary File es un fichero binario que se lee o escribe en bloques de datos. Son más rápidos que los ficheros binarios normales, ya que se leen o escriben en bloques de datos en lugar de leer o escribir byte a byte.

```python
open('file.txt', 'rb')
open('file.txt', 'wb')
```

Con estos tipos de ficheros, se devuelven objetos de tipo `BufferedIOBase`, BufferdReader o BufferedWriter:

```python
>>> file = open('dog_breeds.txt', 'rb')
>>> type(file)
<class '_io.BufferedReader'>
>>> file = open('dog_breeds.txt', 'wb')
>>> type(file)
<class '_io.BufferedWriter'>
```

#### 3.3.3. Ficheros binarios

Un fichero binario en `Raw` es un fichero binario que se lee o escribe byte a byte, generalente usado como bloques de construcción de bajo nivel para flujos de datos binarios más complejos, y por consiguiente no tipicalmente usados.

```python
open('abc.txt', 'rb', buffering=0)
open('abc.txt', 'wb', buffering=0)
```

Estos tipos de ficheros devuelven objetos de tipo `FileIO`:

```python
>>> file = open('dog_breeds.txt', 'rb', buffering=0)
>>> type(file)
<class '_io.FileIO'>
```	

### 3.4. Line Endings

El término `line ending` se refiere a los caracteres que se utilizan para indicar el final de una línea de texto y el comienzo de otra. En Python, los `line endings` se representan como un carácter de nueva línea, que es diferente en diferentes sistemas operativos.

- **Windows**: \r\n
- **Unix/Linux**: \n
- **Mac OS**: \r

Python maneja automáticamente los `line endings` al leer o escribir ficheros. Cuando se lee un fichero, Python convierte automáticamente los `line endings` específicos del sistema operativo en un único carácter de nueva línea (\n). Cuando se escribe un fichero, Python convierte automáticamente el carácter de nueva línea (\n) en el `line ending` específico del sistema operativo.


## 4. No reinventar la rueda. Trabajar con ficheros CSV y Json

Existen muchas situacioes que se requiere el trabajo con Ficheros específicos, y Python ofrece módulos específicos para trabajar con ellos. Dos de los más comunes son los ficheros CSV y JSON.

Además de los ficheros CSV y Json, existen otros tipos de ficheros que Python permiten trabajar con ellos, a través de diferentes módulos:

- **wave**: Ficheros de audio.
- **aifc**: Ficheros de audio.
- **sunau**: Ficheros de audio.
- **tarfile**: Ficheros de compresión.
- **zipfile**: Ficheros de compresión.
- **gzip**: Ficheros de compresión.
- **configparser**: Ficheros de configuración.
- **xml.etree.ElementTree**: Ficheros XML.
- **xml.dom**: Ficheros XML.
- **msilib**: Ficheros MSI.
- **plistlib**: Ficheros de propiedad de Apple.

También exiten otra gran cantidad de tipos de ficheros que pueden adicionalmente ser tratados con Python, a través de módulos de terceros.

- **Pandas**: Ficheros de datos.
- **PyPDF2**: Ficheros PDF.
- **Pillow**: Ficheros de imagen.
- **xlwings**: Ficheros de Excel.

Ahora nos vamos a centrar en los ficheros CSV y Json.

### 4.1. Ficheros CSV

**¿ Qué es un fichero CSV ?**

CSV es un formato de archivo que se utiliza para almacenar datos tabulares, como una hoja de cálculo o una base de datos. Los archivos CSV utilizan `comas` para separar los valores de los campos, y cada fila en el archivo CSV es un registro en la base de datos.

Ejemplo de un fichero CSV:

```csv
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```
Notar que cada fila en el fichero CSV es un registro en la base de datos, y los valores de los campos están separados por comas. La primera fila del fichero CSV es generalmente una fila de encabezado que contiene los nombres de los campos.

El caracter delimitador es llamador `delimiter`, y por defecto es la coma (,). Sin embargo, el delimitador puede ser cualquier carácter, como el punto y coma (;) o el tabulador (\t).

**¿ Quién usa ficheros CSV ?**

Los ficheros CSV son utilizados por una amplia variedad de aplicaciones, incluyendo hojas de cálculo, bases de datos y programas de procesamiento de datos. Los ficheros CSV son fáciles de leer y escribir, y son una forma muy común de intercambiar datos entre aplicaciones.

#### 4.1.1 Leyendo un fichero CSV

Python ofrece un módulo llamado `csv` que proporciona funciones para leer y escribir ficheros CSV. Para leer un fichero CSV en Python, primero necesitamos crear un objeto lector de ficheros CSV y luego leer el contenido del fichero CSV línea por línea.

```python
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
```
La salida de este código sería:

```python
Column names are name, department, birthday month
  John Smith works in the Accounting department, and was born in November.
  Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.
```

Cada fila retornada by el `reader` es una lista de `strings`conteniendo los valores de los campos en esa fila. Al iterar sobre el objeto `reader`, cada fila se devuelve como una lista de `strings`. Para acceder a los valores de los campos en una fila, utilizamos el índice de la lista.

#### Leyebdo un fichero CSV en un diccionario

En lugar de leer un fichero CSV en una lista, podemos leerlo en un diccionario. En este caso, utilizamos el método `DictReader` en lugar del método `reader` (técnicamente como un OrderedDict). De esta forma, los nombres de las columnas se convierten en las claves del diccionario, y los valores de las columnas se convierten en los valores del diccionario.

Veámos el ejemplo anterior, pero ahora leyendo el fichero CSV en un diccionario:

```python
import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
```

**Parámetros opciones de CSV `Reader` y `Writer`**

- Delimitador: Por defecto es la coma (,).
- Quotechar: Por defecto es la comilla doble ("). Espesifica el carácter que se utiliza para rodear los campos que contienen el delimitador.
- Escapechar: Por defecto es None. Especifica el carácter que se utiliza para escapar del delimitador.

Vamos a ver un ejemplo de su uso:

```python
name,address,date joined
john smith,1132 Anywhere Lane Hoboken NJ, 07030,Jan 4
erica meyers,1234 Smith Lane Hoboken NJ, 07030,March 2
```
Este fichero contiene 3 campos, name, address y date joined. El campo address contiene comas, por lo que necesitamos rodear el campo con comillas dobles. El campo date joined contiene espacios, por lo que necesitamos rodear el campo con comillas dobles.

Hay 3 formas de manejar esta situación;

- ***Usar un delimitador diferente***: Podemos usar un delimitador diferente, como el punto y coma (;) o el tabulador (\t). De esta forma, la (,) puede ser usada en los campos sin problemas.
- ***Usar un carácter diferente para rodear los campos***: Podemos usar un carácter diferente para rodear los campos, como el acento grave (`) o el apóstrofe ('). De esta forma, todo lo que esté entre los caracteres de rodeo se considera un campo, incluso si contiene el delimitador.
- ***Escapar del delimitador***: Podemos escapar del delimitador con un carácter de escape, como la barra invertida (\). De esta forma, el delimitador se considera un carácter normal y no un delimitador.

Veámos el ejemplo anterior, pero con cada una de las situaciones:

Con "quotechar":
```python
name,address,date joined
john smith,"1132 Anywhere Lane Hoboken NJ, 07030",Jan 4
erica meyers,"1234 Smith Lane Hoboken NJ, 07030",March 2
```

Con "escapechar":
```python
name,address,date joined
john smith,1132 Anywhere Lane Hoboken NJ\, 07030,Jan 4
erica meyers,1234 Smith Lane Hoboken NJ\, 07030,March 2
```

Con opción "delimiter":
```python
name;aaddress;date joined
john smith;1132 Anywhere Lane Hoboken NJ, 07030;Jan 4
erica meyers;1234 Smith Lane Hoboken NJ, 07030;March 2
```

#### 4.1.2 Escribiendo un fichero CSV

Para escribir un fichero CSV en Python, primero necesitamos crear un objeto escritor de ficheros CSV y luego escribir el contenido del fichero CSV línea por línea.

```python
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
```

El `quotechar` le indica al `writer`cual carctere usar para rodear los campos que contienen el delimitador. El `quoting` le indica al `writer`cuando rodear los campos con el `quotechar`. Los valores posibles son:

- `csv.QUOTE_ALL`: Rodear todos los campos con el `quotechar`.
- `csv.QUOTE_MINIMAL`: Rodear los campos con el `quotechar` solo si contienen el delimitador o el `quotechar`.
- `csv.QUOTE_NONNUMERIC`: Rodear los campos con el `quotechar` solo si no son numéricos.
- `csv.QUOTE_NONE`: No rodear los campos con el `quotechar`.


**Escribiendo un fichero CSV desde un diccionario**

En lugar de escribir un fichero CSV desde una lista, podemos escribirlo desde un diccionario. En este caso, utilizamos el método `DictWriter` en lugar del método `writer`. De esta forma, los nombres de las columnas se convierten en las claves del diccionario, y los valores de las columnas se convierten en los valores del diccionario.

Veámos el ejemplo anterior, pero ahora escribiendo el fichero CSV desde un diccionario:

```python
import csv

with open('employee_file.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
```

> 🚧 **Advertencia**<br>
> También es posible, tratar los ficheros CSV desde Pandas, que es una librería de Python que proporciona estructuras de datos y herramientas de análisis de datos. Pandas es muy útil para leer y escribir ficheros CSV, y proporciona funciones para trabajar con ficheros CSV.

Pero esto sale fuera del alcance de este documento.


### 4.2. Ficheros JSON

**¿ Qué es JSON ?, un poco de historia**

JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero y fácil de leer. Fue creado por Douglas Crockford en 2001. JSON es un formato de texto que es completamente independiente del lenguaje, pero utiliza convenciones que son familiares para los programadores de la familia de lenguajes C, incluyendo C, C++, C#, Java, JavaScript, Perl, Python y muchos otros. Estas propiedades hacen que JSON sea un lenguaje ideal para el intercambio de datos.

Veámos un ejemplo, de un fichero JSON:

```json
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

Como se puede ver, JSON soporta tipos de datos primitivos, como cadenas de texto y números, así como tipos de datos anidados, como objetos y listas.


#### 4.2.1. Python soporta nativamente JSON

Python tiene un módulo incorporado llamado `json` que se puede utilizar para trabajar con datos JSON.

**Un poco de Cultura**

El proceso de encoding de un objeto en un formato JSON se llama `serialization`, y el proceso de decoding de un objeto JSON se llama `deserialization`. Este término se aplica a la conversión de datos en un formato que puede ser almacenado o transmitido y luego reconstruido, como por ejemplo, enviado a través de una red y almacenado en un fichero, o enviando datos a través de una red.

**Serialización JSON**

Los tipos simples de Python son transformados en tipos simples de JSON de la siguiente manera:

- `None` se convierte en `null`.
- `True` se convierte en `true`, y `False` se convierte en `false`.
- Los números enteros, flotantes y decimales se convierten en `numbers` (números) en JSON.
- Las cadenas de texto se convierten en cadenas de texto JSON. (`string` en JSON).
- diccionarios se convierten en objetos JSON.
- listas y tuplas se convierten en arrays JSON.

Si partimos de este diccionario:

```python
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
```

La idea es almacenar este diccionario en un fichero JSON. Para ello, utilizamos el método `dump()` del módulo `json`.

```python
import json

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
``` 

Notar que el método `dump()` toma dos argumentos, el objeto a serializar y el fichero en el que se va a almacenar el objeto serializado.

También existe el método `dumps()` que toma un objeto y devuelve una cadena de texto JSON.

Tabla diferencias entre `dump()` y `dumps()`, comparando cada métodos lado a lado.

| dump() | dumps() |
|--------|---------|
| Toma un objeto y un fichero. | Toma un objeto y devuelve una cadena de texto. |
| Almacena el objeto serializado en un fichero. | Devuelve el objeto serializado como una cadena de texto. |
| Se utiliza para almacenar datos JSON en un fichero. | Se utiliza para enviar datos JSON a través de una red. |

**Deserialización JSON**

Justo como la serialización, la deserialización es un proceso simple. Si tenemos un fichero JSON, podemos leer el contenido del fichero y deserializarlo en un objeto Python utilizando el método `load()`.

```python
import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)
```
Tamibén existe el método `loads()` que toma una cadena de texto JSON y devuelve un objeto Python.

```python
import json

# Some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

La serialización y deserilización es muy útil cuando se quieren enviar datos a través de una red, o almacenar datos en un fichero.

