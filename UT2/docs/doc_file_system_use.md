<!-- omit in toc -->
# Sistema de ficheros en Python


<!-- omit in toc -->
## Indice 

- [Introducción](#introducción)
  - [Normalización de las ruta](#normalización-de-las-ruta)
- [Obteniendo listado de ficheros y directorios](#obteniendo-listado-de-ficheros-y-directorios)
  - [Listar carpetas y ficheros en versiones modernas de Python](#listar-carpetas-y-ficheros-en-versiones-modernas-de-python)
  - [Listar todos los ficheros en un directorio](#listar-todos-los-ficheros-en-un-directorio)
  - [Listar ficheros de un directorio recursivamente](#listar-ficheros-de-un-directorio-recursivamente)
- [Obtener los atributos de los ficheros](#obtener-los-atributos-de-los-ficheros)
- [Crear y eliminar directorios](#crear-y-eliminar-directorios)
- [Pattern Matching](#pattern-matching)
- [Recorriendo directorios y procesando ficheros](#recorriendo-directorios-y-procesando-ficheros)
- [Borrando ficheros y directorios](#borrando-ficheros-y-directorios)
  - [Borrando ficheros](#borrando-ficheros)
  - [Borrando directorios](#borrando-directorios)
- [Copiando, moviendo y renombrando ficheros y directorios](#copiando-moviendo-y-renombrando-ficheros-y-directorios)
  - [Copiando ficheros](#copiando-ficheros)
  - [Copiando directorios](#copiando-directorios)
  - [Moviendo y renombrando ficheros y directorios](#moviendo-y-renombrando-ficheros-y-directorios)
  - [Renombrando ficheros y directorios](#renombrando-ficheros-y-directorios)


## Introducción

El módulo `os` proporciona una forma sencilla de interactuar con el sistema de ficheros. A través de `os` podemos obtener el listado de ficheros y directorios, obtener los atributos de los ficheros, crear y eliminar directorios, buscar ficheros y directorios que coincidan con un patrón determinado, recorrer directorios y procesar ficheros, y copiar, mover y renombrar ficheros y directorios.

Además del módulo `os`, el módulo `pathlib` proporciona una forma más orientada a objetos de interactuar con el sistema de ficheros. A través de `pathlib` podemos trabajar con rutas de forma más sencilla y segura, y realizar operaciones con ficheros y directorios de forma más eficiente.	

También otros módulos como el módulo `shutil` proporciona una forma sencilla de copiar, mover y eliminar ficheros y directorios.

### Normalización de las ruta

Uno de los principales problemas al trabajar con ficheros y directorios es la normalización de las rutas. La normalización de rutas es el proceso de convertir una ruta en una forma estandarizada. Por ejemplo, en Windows, la ruta `C:\Users\user\Documents` es la misma que `C:/Users/user/Documents`, pero en Linux y macOS, la ruta `C:\Users\user\Documents` no es la misma que `C:/Users/user/Documents`. La normalización de rutas es importante para que nuestro código sea portable, es decir, que funcione en cualquier sistema operativo.

Además de que Windows no distingue entre mayúsculas y minúsculas en las rutas, mientras que Linux y macOS sí lo hacen, otro factor muy importante son los separadores de rutas. En Windows, el separador de rutas es `\` (barra invertida), mientras que en Linux y macOS es `/` (barra normal). La normalización de rutas se encarga de convertir las barras invertidas en barras normales, y de convertir las rutas en una forma estandarizada.

El módulo `os.path` proporciona funciones para trabajar con rutas de forma segura y portátil. A través de `os.path` podemos normalizar rutas, unir rutas, separar rutas, obtener el nombre del fichero, obtener la extensión del fichero, comprobar si una ruta es absoluta, comprobar si una ruta existe, comprobar si una ruta es un directorio, comprobar si una ruta es un fichero, y comprobar si una ruta es un enlace simbólico.

Para normalizar una ruta, podemos utilizar la función `os.path.normpath()`. Este método retorna un string que representa la ruta normalizada.

```python
import os

os.path.normpath(r'C:\Users\user\Documents')
# 'C:\\Users\\user\\Documents'
os.path.normpath(r'C:/Users/user/Documents')  # En Windows, la convierte en una ruta normalizada con los separadores de rutas correctos
# 'C:\\Users\\user\\Documents'
```

> 🔥 **Importante**<br>
> Para poder indicar una ruta con la barra invertida (\) en Python, es necesario indicar la letra `r` delante de la cadena de texto, para que Python interprete la cadena de texto como una cadena de texto cruda (raw string). Esto es necesario porque el carácter `\` es un carácter de escape en Python, y si no se indica la letra `r` delante de la cadena de texto, Python interpretará la cadena de texto de forma incorrecta.

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

<!-- omit in toc -->
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

<!-- omit in toc -->
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

Para buscar ficheros y directorios que coincidan con un patrón determinado podemos hacer lo siguiente:

1. **Utilizando los métodos propios del tipo *strings* `endswith()` y `startswith()`:**

    ```python
    import os

    # Obtener todos los ficheros/directorios en la carpeta actual
    for f_name in os.listdir('.'):
        if os.path.isfile(f_name) and f_name.endswith('.py'):
            print(f_name)   

    ```

2. **Utilizando `os.fnmatch`:**

    El módulo fnmatch proporciona dos funciones para buscar ficheros y directorios que coincidan con un patrón determinado:

    - `fnmatch()`: determina si un nombre de fichero coincide con un patrón determinado. No distingue entre mayúsculas y minúsculas.
    - `fnmatchcase()`: determina si un nombre de fichero coincide con un patrón determinado, *respetando mayúsculas y minúsculas*.

    ```python
    import os

    # Obtener todos los ficheros/directorios en la carpeta actual
    for f_name in os.listdir('.'):
        if os.path.isfile(f_name) and os.fnmatch(f_name, '*.py'):
            print(f_name)   
    ```


3. **Utilizando `filter()`**
   
    Filter es una función que permite filtrar los elementos de una secuencia, en este caso, una lista de ficheros y directorios.

    ```python
    import os

    # Obtener todos los ficheros/directorios en la carpeta actual
    files = os.listdir('.')
    files_fitlered = filter(files, "*.py")  # Devuelve un iterador

    for f_name in filter(files, "*.py")
        print(f_name)
    ```

    Filter acepta `wildcards` como `*` y `?` para buscar ficheros y directorios que coincidan con un patrón determinado.

    También se pueden indicar multi-filtros, separados por |, por ejemplo: `*.py|*.txt`


4. **Utilizando `glob()`**

    Otra opción para buscar ficheros y directorios que coincidan con un patrón determinado es utilizar la función `glob()`.

    `glob()` está dentro del módulo `glob` y functiona como `fnmatch` pero difiere en que `fnmatch()` solo busca en el directorio actual, `glob()` busca en todos los subdirectorios (Si se indica).

    UNIX y sistemas basados en unix trasladan patrones de búsqueda con comodines a la shell antes de que el comando sea ejecutado. Esto significa que los comodines son expandidos por la shell antes de que el comando sea ejecutado. Por ejemplo, `ls *.py` se convierte en `ls file1.py file2.py` antes de que el comando sea ejecutado. **ESTO ES LLAMADO GLOBBING**.

    En el siguiente ejemplo use usa `glob()` para buscar ficheros y directorios que coincidan con un patrón determinado:

    ```python
    import glob

    for f_name in glob.glob('*.py'):
        print(f_name)
    ```

    Glob también permite la búsqueda aplicando comodines, tipo expresiones regulares, por ejemplo:

    ```python
    import glob

    for f_name in glob.glob('*[0-9]*.txt'):  # Busca ficheros que contengan un número en su nombre
        print(f_name)
    ```

    En el ejemplo anterior no hay diferencia con `filter` o `fnmatch`, pero si se quiere buscar en subdirectorios, de forma recursiva, se puede hacer lo siguiente:

    ```python
    import glob

    for f_name in glob.glob('**/*.py', recursive=True): # Busca ficheros .py en todos los subdirectorios
        print(f_name)
    ```

    A través del parámetro `recursive` se puede buscar en todos los subdirectorios de forma recursiva.

    > 💡 **Nota**<br>
    > `glob()` solo está disponible a partir de Python 3.5.


## Recorriendo directorios y procesando ficheros

Una tarea común en programación es recorrer a arból de directorios y procesar los ficheros que se encuentran en ellos. La función `os.walk()` nos permite recorrer un directorio y sus subdirectorios de forma recursiva.

Esta functión nos permite recorrer un arból de directorios, tanto de arriba hacía abajo como de abajo hacía arriba, y nos devuelve una tupla con tres elementos:

- 1º: directorio-actual El primer elemento es una cadena de texto que representa el directorio actual.
- 2º: Lista subdirectorios del directorio actual.
- 3º: Lista de los ficheros del directorio actual.

Para los ejemplos vamos a utilizar la siguiente estructura de directorios y ficheros:

```plaintext
.
|
├── folder_1/
|   ├── file1.py
|   ├── file2.py
|   └── file3.py
|
├── folder_2/
|   ├── file4.py
|   ├── file5.py
|   └── file6.py
|
├── test1.txt
└── test2.txt
```

Por defecto, `os.walk()` recorre el directorio de arriba hacía abajo, es decir, primero recorre los subdirectorios y luego los ficheros.

```python
import os

for dirpath, dirnames, filenames in os.walk('.'):
    print(f'En el directorio {dirpath} hay {len(filenames)} ficheros')
    for filename in filenames:
        print(filename)
```

Para recorre el directorio de abajo hacía arriba, es decir, primero recorre los ficheros y luego los subdirectorios, le pasamos el argumento `topdown=False` a `os.walk()`:

```python
import os

for dirpath, dirnames, filenames in os.walk('.', topdown=False):
    print(f'En el directorio {dirpath} hay {len(filenames)} ficheros')
    for filename in filenames:
        print(filename)
```

Para recorrer un directorio y sus subdirectorios de forma recursiva y procesar los ficheros que se encuentran en ellos, podemos hacer lo siguiente:

```python
import os

def recorrer_directorio(directorio):
    
    for dirpath, dirnames, filenames in os.walk(directorio):
        print(f'En el directorio {dirpath} hay {len(filenames)} ficheros')
        for filename in filenames:
            print(filename)

        for dirname in dirnames:
            recorrer_directorio(dirname)

```

## Borrando ficheros y directorios

Se pueden borrar un solo fichero o directorio, o borrar varios ficheros o toda una jerarquía de directorios, usando los métodos encontrados dentro del módulo `os`:

- `os.remove(), os.unlink()`: Borra un fichero, y dan error si el es un directorio o si no existe.
- `os.rmdir()`: Borra un directorio.
- `shutil.rmtree()`: Borra un directorio y todos los ficheros y subdirectorios que contiene.
- `os.removedirs()`: Borra un directorio y todos los directorios intermedios.


### Borrando ficheros

Para borrar un único fichero, se puede usar `os.remove()`. Es fundamental indicar correctamente la ruta, que puede ser relativa o absoluta. Para indicar una ruta relativa, se puede indicar usando el "./" delante del nombre del fichero (aunque no es necesario).

```python
import os

os.remove('./file1.txt') # Ambas líneas son equivalentes
os.unlink('./file1.txt')
```

Al borrar un fichero, siempre hay que controlar los errores, ya que si el fichero no existe, o está en uso, o no se tiene permisos, se producirá un error.

```python
import os

try:
    os.remove('./file1.txt')
except FileNotFoundError:
    print('El fichero no existe')
except IsADirectoryError:
    print('El fichero es un directorio')
except PermissionError:
    print('No tienes permisos para borrar el fichero')
except OSError:
    print('El fichero está en uso')
Except Exception as e:
    print(f'Error desconocido: {e}')
```

### Borrando directorios

La librería estándar de Python proporciona una serie de métodos para borrar directorios:

- `os.rmdir(), pathlib.rmdir()`: Borra un directorio. Si el directorio no está vacío, se producirá un error.
- `os.removedirs()`: Borra un directorio y todos los directorios intermedios. Si el directorio no está vacío, se producirá un error.


```python
import os
from pathlib import Path

os.rmdir('./mydir') # Borra el directorio mydir

# Con pathlib
trash_dir = Path('./mydir')
trash_dir.rmdir()
```

<!-- omit in toc -->
#### Borrando arból de directorios

Para borrar un directorio y todos los ficheros y subdirectorios que contiene, se puede usar `shutil.rmtree()`.

```python
import shutil

shutil.rmtree('./mydir') # Borra el directorio mydir y todos los ficheros y subdirectorios que contiene
```

Si se desea realizar el borrado de forma controlada, se puede realizar realizando de forma recursiva utilizando `os.walk()` y `os.remove()`.

```python
import os

def borrar_directorio(directorio):
    for dirpath, dirnames, filenames in os.walk(directorio, topdown=False):
        for filename in filenames:
            os.remove(os.path.join(dirpath, filename))
        for dirname in dirnames:
            borrado_directorio(os.path.join(dirpath, dirname))  # Llamada recursiva
            os.rmdir(os.path.join(dirpath, dirname)) # Una vez borrado todos sus ficheros y directorios que contiene, se borra el directorio

    os.rmdir(directorio)  # Finalmente se borra el directorio raíz
```

## Copiando, moviendo y renombrando ficheros y directorios

La librería estándar de Python proporciona una serie de métodos para copiar, mover y renombrar ficheros y directorios:

- `shutil.copy()`: Copia un fichero.
- `shutil.copy2()`: Copia un fichero y mantiene los metadatos.
- `shutil.copytree()`: Copia un directorio y todos los ficheros y subdirectorios que contiene.
- `shutil.move()`: Mueve un fichero o directorio.
- `os.rename()`: Renombra un fichero o directorio.
- `os.replace()`: Reemplaza un fichero o directorio.
- `os.link()`: Crea un enlace duro a un fichero o directorio.
- `os.symlink()`: Crea un enlace simbólico a un fichero o directorio.
- `os.readlink()`: Lee el destino de un enlace simbólico.


### Copiando ficheros

Shutil proporciona dos métodos para copiar ficheros:

- `shutil.copy()`: Copia un fichero.
- `shutil.copy2()`: Copia un fichero y mantiene los metadatos.

```python
import shutil

shutil.copy('./file1.txt', 'path/to/folder/file2.txt') # Copia el fichero file1.txt a path/to/folder/file2.txt
shutil.copy2('./file1.txt', 'path/to/folder/file2.txt') # Copia el fichero file1.txt a path/to/folder/file2.txt y mantiene los metadatos
```
`copy` es comparable al comando `cp` de UNIX, mientras que `copy2` es comparable al comando `cp -p` de UNIX. (El comando `cp -p` mantiene los metadatos del fichero original).

### Copiando directorios

Mientras que `copy` solo copian un único fichero, `copytree` copia un directorio y todos los ficheros y subdirectorios que contiene. Toma 2 argumentos, el directorio origen y el directorio destino.

```python
import shutil

shutil.copytree('./mydir', 'path/to/folder/mydir_backup') # Copia el directorio mydir a path/to/folder/mydir
```
> 💡 **Nota**<br>
> Si el directorio destino ya existe, se producirá un error.
> Si la ruta hasta la carpeta destino no existe, se creará.

### Moviendo y renombrando ficheros y directorios

Para mover un fichero o directorio a otro ubicación, usar `shutil.move()`. Toma 2 argumentos, el fichero origen y el fichero destino.

*Si el directorio destino no existe, se creará. Si el directorio destino ya existe, el contenido del directorio origen se moverá al directorio destino.*

```python
import shutil

shutil.move('./file1.txt', 'path/to/folder/file2.txt') # Mueve el fichero file1.txt a path/to/folder/file2.txt
shutil.move('mydir/', 'mydir_backup/') # Mueve (renombrar) el directorio mydir a mydir_backup
```

### Renombrando ficheros y directorios

Para renombrar un fichero o directorio, usar `os.rename()`. Toma 2 argumentos, el fichero origen y el fichero destino.

```python
import os

os.rename('./file1.txt', './file2.txt') # Renombra el fichero file1.txt a file2.txt
```	

> 🔥 **Importante** <br>
> No se puede convertir un fichero en un directorio y a la inversa, con rename o con move, ya que se producirá un error.

