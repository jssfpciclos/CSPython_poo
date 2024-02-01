# Sistema de ficheros en Python


## Obteniendo listado de ficheros y directorios

Suponer que nuestro actual directorio tiene un subdirectorio llamado `mydir` que tiene el siguiente contenido:

```
mydir/
|
├── sub_dir/
|   ├── bar.py
|   └── foo.py
|
├── sub_dir_b/
|   └── file4.txt
|
├── sub_dir_c/
|   ├── config.py
|   └── file5.txt
|
├── file1.py
├── file2.csv
└── file3.txt
```

El `os` módulo proporciona funciones para interactuar con el sistema operativo. Por ejemplo, para obtener el listado de ficheros y directorios de un directorio podemos utilizar la función `os.listdir()`:

```python
import os

os.listdir('mydir/')
# ['sub_dir', 'sub_dir_b', 'sub_dir_c', 'file1.py', 'file2.csv', 'file3.txt']
```

`os.listdir()` retorna una lista que contiene los nombres de los ficheros y carpetas en el directorio pasado como argumento.


Si queremos obtener el listado de ficheros y directorios de un directorio que está en otro directorio, podemos utilizar la función `os.path.join()` para construir la ruta completa:

```python
import os

os.listdir(os.path.join('mydir', 'sub_dir'))
# ['bar.py', 'foo.py']
```

Esto permite que nuestro código sea portable, es decir, que funcione en cualquier sistema operativo, ya que la función `os.path.join()` construye la ruta de forma correcta dependiendo del sistema operativo en el que se ejecute el código.

> 💡 **Nota**<br>
> En Windows, la ruta de los ficheros y directorios se separa con el carácter `\` (barra invertida), mientras que en Linux y macOS se utiliza el carácter `/` (barra normal). La función `os.path.join()` se encarga de construir la ruta de forma correcta dependiendo del sistema operativo en el que se ejecute el código.


### Listar carpetas y ficheros en versiones modernas de Python


#### os.scandir()

En versiones modernas de Python (3.5+) una alternativa a `os.listdir()` es utilizar la función `os.scandir()`.

`os.scanir()` retorna un iterador que produce objetos de tipo `DirEntry` que contienen información sobre los ficheros y directorios del directorio pasado como argumento.

```python
import os

with os.scandir('mydir/') as entries:
    for entry in entries:
        print(entry.name)
# sub_dir 
# sub_dir_b
# sub_dir_c
# file1.py
# file2.csv
# file3.txt
```

En el ejemplo anterior hemos utilizado un gestor de contexto para asegurarnos que el iterador se cierra correctamente al finalizar el bucle.

El objeto `DirEntry` tiene los siguientes atributos:

- `name`: nombre del fichero o directorio.
- `path`: ruta completa del fichero o directorio.
- `inode`: número de identificación del fichero o directorio.
- `is_dir()`: método que retorna `True` si el objeto es un directorio.
- `is_file()`: método que retorna `True` si el objeto es un fichero.
- `is_symlink()`: método que retorna `True` si el objeto es un enlace simbólico.
- `stat()`: método que retorna un objeto `os.stat_result` con información sobre el fichero o directorio.

```python
import os

with os.scandir('mydir/') as entries:
    for entry in entries:
        print(entry.name, entry.path, entry.is_dir(), entry.is_file())
# sub_dir mydir/sub_dir True False  
# sub_dir_b mydir/sub_dir_b True False
...
```

#### **iterdir()**

A partir de la versión 3.6+ podemos utilizar la función `pathlib.Path.iterdir()` para obtener un iterador con los ficheros y directorios de un directorio.

```python
from pathlib import Path

for entry in Path('mydir/').iterdir():
    print(entry.name)
# sub_dir
# sub_dir_b
...
```

En resumen, usar `os.scandir()` o `pathlib.Path.iterdir()` es más eficiente que `os.listdir()` ya que no se crea una lista con todos los ficheros y directorios del directorio, sino que se crea un iterador que produce los ficheros y directorios a medida que se van necesitando.

En la siguiente tabla se realiza una comparación entre las funciones `os.listdir()`, `os.scandir()` y `pathlib.Path.iterdir()`:

| Función | Versión | Tipo de retorno | ¿Crea una lista? |
|---------|---------|-----------------|------------------|
| `os.listdir()` | Todas | Lista | Sí |
| `os.scandir()` | 3.5+ | Iterador | No |
| `pathlib.Path.iterdir()` | 3.6+ | Iterador | No |



### Listar todos los ficheros en un directorio

Cuando queremos listar todos los ficheros de un directorio, y filtrar si solo queremos ficheros, o directorios o incluso ficheros con una extensión determinada, podemos combinar las técnicas anteriores con la función `os.path.isfile()`.

Por ejemplo, para listar todos los ficheros de un directorio podemos hacer lo siguiente:

```python
import os

for entry in os.scandir('mydir/'):
    if entry.is_file():
        print(entry.name)
# file1.py
# file2.csv
...
```

Para listar todos los directorios de un directorio podemos hacer lo siguiente:

```python
import os

for entry in os.scandir('mydir/'):
    if entry.is_dir():
        print(entry.name)
# sub_dir
# sub_dir_b
...
```

Para listar todos los ficheros con una extensión determinada podemos hacer lo siguiente:

```python
import os

for entry in os.scandir('mydir/'):
    if entry.is_file() and entry.name.endswith('.txt'):
        print(entry.name)
# file3.txt
...
```

### Listar ficheros de un directorio recursivamente

Para listar todos los ficheros de un directorio y sus subdirectorios podemos combinar las técnicas anteriores, y usar la recursividad.

En el siguiente ejemplo se muestra una función que muestra el contenido de un directorio dado, en una forma recursiva, similar al comando `tree` de Linux, anexando los niveles de profundidad visualmente a través de la indentación y las líneas verticales:

```python
import os

def tree(dir, level=0):
    for entry in os.scandir(dir):
        if entry.is_dir():
            print('|   ' * level + '|-- ' + entry.name)
            tree(entry.path, level + 1)
        else:
            print('|   ' * level + '|-- ' + entry.name)

tree('mydir/')
# |-- sub_dir
#   |-- bar.py
#   |-- foo.py
# |-- sub_dir_b
...
```

## Obtener los atributos de los ficheros

El módulo `os` proporciona funciones para obtener los atributos de los ficheros y directorios.

A través de `stat()` podemos obtener los atributos de un fichero o directorio:

```python
import os

with os.scandir('mydir/') as entries:
    for entry in entries:
        info = entry.stat()
        print(entry.name, info.st_size, info.st_mtime)
# sub_dir 4096 1610395200.0
# sub_dir_b 4096 1610395200.0
# sub_dir_c 4096 1610395200.0
...
```

El objeto `os.stat_result` tiene muchos atributos que nos permiten obtener información sobre el fichero o directorio, para más información consultar la [documentación oficial](https://docs.python.org/3/library/os.html#os.stat_result).


## Crear y eliminar directorios

Crear y eliminar directorios es muy sencillo con el módulo `os`.

En la siguiente tabla se recopila las distintas opciones para crear y eliminar directorios:

| Función | Descripción |
|---------|-------------|
| `os.mkdir()` | Crea un directorio. |
| `os.makedirs()` | Crea un directorio y todos los directorios intermedios. |
| `os.rmdir()` | Elimina un directorio. |
| `os.removedirs()` | Elimina un directorio y todos los directorios intermedios. |

Por ejemplo, para crear un directorio podemos hacer lo siguiente:

```python
import os

os.mkdir('mydir2')
```

> 💡 **Recordar**<br>
> Si el directorio ya existe, se producirá un error.

Para crear una estructura de directorios podemos hacer lo siguiente, utilizando módulo `os.path.join()` para construir la ruta completa:

```python
import os

os.makedirs(os.path.join('mydir2', 'sub_dir', 'sub_dir_b'))
```

Otra opción para crear una estructura de directorios es utilizar la función `pathlib.Path.mkdir()`:

```python
from pathlib import Path

Path('mydir2/sub_dir/sub_dir_b').mkdir(parents=True)
```

Para eliminar un directorio podemos hacer lo siguiente:

```python
import os

os.rmdir('mydir2')
```

## Pattern Matching

Otra de las funcionalidades que nos proporciona el módulo `os` es la posibilidad de buscar ficheros y directorios que coincidan con un patrón determinado.

Las funciones que nos permiten buscar ficheros y directorios son:

- `os.fnmatch()`: determina si un nombre de fichero coincide con un patrón determinado.
- `os.fnmatchcase()`: determina si un nombre de fichero coincide con un patrón determinado, respetando mayúsculas y minúsculas.
- `endswith() y startswith()`: determina si un nombre de fichero termina o empieza con un patrón determinado.
- `glob()`: busca ficheros y directorios que coincidan con un patrón determinado.

Cada uno de los siguientes ejemplos los basaremos en la siguiente estructura de directorios y ficheros:

```
.
|
├── sub_dir/
|   ├── file1.py
|   └── file2.py
|
├── admin.py
├── data_01_backup.txt
├── data_01.txt
├── data_02_backup.txt
├── data_02.txt
├── data_03_backup.txt
├── data_03.txt
└── tests.py
```










