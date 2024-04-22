<!-- omit in toc -->

# Ficheros de configuración en Python

Un fichero de configuración es un fichero que contiene información que se utiliza para configurar un programa. Los ficheros de configuración son muy útiles para almacenar información que no cambia con frecuencia, como la configuración de un programa, la configuración de un servidor, la configuración de una base de datos, etc.

También se utilizan para poder modificar el comportamiento de un programa, sin tener que modificar el código fuente del programa. Por ejemplo, si un programa se conecta a una base de datos, se puede almacenar la información de conexión en un fichero de configuración, de esta forma, si la información de conexión cambia, no es necesario modificar el código fuente del programa, sino que se puede modificar el fichero de configuración.

<!-- omit in toc -->

## Indice

- [Ficheros INI](#ficheros-ini)
  - [ConfigParser](#configparser)
    - [Escribir ficheros INI](#escribir-ficheros-ini)
- [Ficheros YAML](#ficheros-yaml)
  - [PyYAML](#pyyaml)
- [Ficheros JSON](#ficheros-json)
- [Ficheros XML](#ficheros-xml)

## Ficheros INI

Un fichero INI es un fichero de texto que contiene una serie de secciones, cada una de las cuales contiene una serie de claves y valores. Los ficheros INI son muy utilizados para almacenar información de configuración, como la configuración de un programa, la configuración de un servidor, la configuración de una base de datos, etc.

Ejemplo de un fichero INI:

```ini
[database]
host = localhost
port = 3306
user = root
password = password

[server]
host = localhost
port = 8080
```

En el ejemplo anterior, el fichero INI contiene dos secciones, `database` y `server`, cada una de las cuales contiene una serie de claves y valores. Por ejemplo, la sección `database` contiene las claves `host`, `port`, `user` y `password`, cada una de las cuales tiene un valor asociado.

Python proporciona el módulo `configparser` para trabajar con ficheros INI. A través de `configparser` podemos leer y escribir ficheros INI, y obtener y modificar los valores de las claves.

### ConfigParser

El módulo `configparser` proporciona una clase llamada `ConfigParser` que se utiliza para leer y escribir ficheros INI. Para leer un fichero INI, se crea un objeto de la clase `ConfigParser` y se llama al método `read()` pasando la ruta del fichero INI como argumento. Para obtener un valor de una clave, se llama al método `get()` pasando el nombre de la sección y el nombre de la clave como argumentos.

```python
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

host = config.get('database', 'host')
port = config.get('database', 'port')
user = config.get('database', 'user')
password = config.get('database', 'password')

print(host, port, user, password)
```

En el ejemplo anterior, se crea un objeto de la clase `ConfigParser` y se llama al método `read()` pasando la ruta del fichero INI como argumento. Luego, se llama al método `get()` pasando el nombre de la sección y el nombre de la clave como argumentos para obtener los valores de las claves.

Es posible también obtener los valores de todas las claves de una sección llamando al método `items()` pasando el nombre de la sección como argumento. El método `items()` devuelve una lista de tuplas, donde cada tupla contiene el nombre de la clave y el valor de la clave.

```python
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

for key, value in config.items('database'):
    print(key, value)
```

Si algún valor no está definido en el fichero INI, se puede establecer un valor por defecto llamando al método `get()` pasando el nombre de la sección, el nombre de la clave y el valor por defecto como argumentos.

```python
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

host = config.get('database', 'host', fallback='localhost')
port = config.get('database', 'port', fallback='3306')
user = config.get('database', 'user', fallback='root')
password = config.get('database', 'password', fallback='password')

print(host, port, user, password)
```

### Escribir ficheros INI

Para escribir un fichero INI, se llama al método `write()` pasando un objeto de la clase `ConfigParser` como argumento. Luego, se llama al método `set()` pasando el nombre de la sección, el nombre de la clave y el valor como argumentos para establecer los valores de las claves.

```python
import configparser

config = configparser.ConfigParser()

config['database'] = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': 'password'
}

config['server'] = {
    'host': 'localhost',
    'port': '8080'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
```

En el ejemplo anterior, se crea un objeto de la clase `ConfigParser` y se establecen los valores de las claves llamando al método `set()`. Luego, se llama al método `write()` pasando un objeto de la clase `ConfigParser` como argumento para escribir el fichero INI.

## Ficheros YAML

YAML (YAML Ain't Markup Language) es un formato de serialización de datos legible por humanos que se utiliza para representar datos de forma estructurada. YAML es muy utilizado para almacenar información de configuración.

YAML tiene las siguientes reglas:

- Los datos se representan como pares clave-valor.
- Los pares clave-valor se separan por dos puntos `:`.
- La relación jerárquica entre los datos se representa mediante la indentación.
- Las listas se representan mediante guiones `-`.
- Los comentarios se representan mediante el carácter `#`.

Ejemplo de un fichero YAML:

```yaml
database:
  host: localhost
  port:
    - 3306
    - 3307
  user: root
  password: password

server:
  host: localhost
  port: 8080
```

En el ejemplo anterior, el fichero YAML contiene dos claves, `database` y `server`, cada una de las cuales contiene una serie de pares clave-valor. Por ejemplo, la clave `database` contiene las claves `host`, `port`, `user` y `password`, cada una de las cuales tiene un valor asociado.

Python no tiene soporte nativo para ficheros YAML, pero se puede utilizar la librería `PyYAML` para trabajar con ficheros YAML. A través de `PyYAML` podemos leer y escribir ficheros YAML, y obtener y modificar los valores de las claves.

### PyYAML

La librería `PyYAML` proporciona una clase llamada `YAML` que se utiliza para leer y escribir ficheros YAML. Para leer un fichero YAML, se crea un objeto de la clase `YAML` y se llama al método `load()` pasando un objeto de la clase `file` como argumento. Para obtener un valor de una clave, se accede al objeto de la clase `dict` devuelto por el método `load()`.

```python
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

    host = config['database']['host']
    port = config['database']['port']
    user = config['database']['user']
    password = config['database']['password']

    print(host, port, user, password)
```

El `loader` es un argumento opcional que se puede pasar al método `load()` para especificar el tipo de loader que se va a utilizar. En el ejemplo anterior, se utiliza el loader `FullLoader` que carga el fichero YAML de forma segura.

También existen otros loaders que se pueden utilizar, como `SafeLoader`, `Loader` y `BaseLoader`. El loader `SafeLoader` es el más seguro, ya que no permite la ejecución de código Python en el fichero YAML.

La información cargada es tratada como un `diccionario` y se puede acceder a los valores de las claves utilizando la notación de corchetes `[]`.

```python
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

    for key, value in config['database'].items():
        print(key, value)
```

Si algún valor no está definido en el fichero YAML, se puede establecer un valor por defecto utilizando la notación de corchetes `[]`.

```python
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

    host = config['database'].get('host', 'localhost')
    port = config['database'].get('port', '3306')
    user = config['database'].get('user', 'root')
    password = config['database'].get('password', 'password')

    print(host, port, user, password)
```

## Ficheros JSON

Aunque no es tan habitual como los ficheros INI o YAML, también es posible utilizar ficheros JSON para almacenar información de configuración. JSON (JavaScript Object Notation) es un formato de serialización de datos que se utiliza para representar datos de forma estructurada.

Para leer un fichero JSON, ya se ha visto en los puntos anteriores de este tema, utilizando la librería `json` de Python. A través de `json` podemos leer y escribir ficheros JSON, y obtener y modificar los valores de las claves.

## Ficheros XML

XML (eXtensible Markup Language) es un formato de serialización de datos que se utiliza para representar datos de forma estructurada. XML es muy utilizado para almacenar información de configuración.

XML es cada vez menos utilizado en favor de JSON o YAML, pero aún se puede encontrar en algunos sistemas heredados. Debido a su complejidad, no lo vamos a abordar en este tema, pero se puede utilizar la librería `xml.etree.ElementTree` de Python para trabajar con ficheros XML.
