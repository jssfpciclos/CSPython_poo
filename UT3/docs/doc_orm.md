<!-- omit in toc -->

# ORM (Object-Relational Mapping)

Un ORM (Object-Relational Mapping) es una técnica de programación que permite a los desarrolladores de software trabajar con bases de datos relacionales utilizando objetos en lugar de sentencias SQL. Un ORM mapea las tablas de una base de datos a clases de un lenguaje de programación, y las filas de las tablas a objetos de las clases.

<!-- omit in toc -->
## Indice

- [ORM (Object-Relational Mapping)](#orm-object-relational-mapping)
  - [Introducción](#introducción)
    - [Qué es un ORM](#qué-es-un-orm)
    - [Popular ORM en Python](#popular-orm-en-python)
    - [Ventajas y Desventajas de ORM](#ventajas-y-desventajas-de-orm)
      - [Ventajas](#ventajas)
      - [Desventajas](#desventajas)
  - [PEEWEE](#peewee)
    - [Siguientes pasos](#siguientes-pasos)
    - [Ejemplo de uso](#ejemplo-de-uso)
    - [Referencias](#referencias)
    - [Ejemplos](#ejemplos)

## Introducción

El problema del acceso a BD es que las bases de datos relacionales utilizan un modelo de datos basado en tablas, mientras que los lenguajes de programación utilizan un modelo de datos basado en objetos. Esto hace que sea difícil trabajar con bases de datos relacionales en lenguajes de programación orientados a objetos, como Python.

Es lo que se llama MisMatch de Modelos de Datos. Es decir, que el modelo relacional donde prima la normalización y la integridad referencial, y se dividen los datos en diferentes tablas, que hace mucho más dificil trabajar con los datos, como si estos estuvieran agrupados todos juntos.

Para resolver este problema, se han desarrollado los ORM, que permiten a los desarrolladores de software trabajar con bases de datos relacionales utilizando objetos en lugar de sentencias SQL. 

### Qué es un ORM

ORM es una técmica de programación para mapear objetos a tablas de bases de datos relacionales. Hay a diferencia significativa entre object-oriented y databases relacionales.  Las BD relacionales se organizan en filas y columnas, donde cada fila tiene un identificador unico (clave primeria) y cada columna tiene un nombre y tipo de datos. De esta forma, se tiene una estructura tabular, donde cada fila es un registro y cada columna es un campo. En caso de que una columna no tenga valor, se le asigna un valor nulo.

Por otro lado, los lenguajes de programación orientados a objetos, se organizan en clases y objetos. Las clases son plantillas que definen los atributos y métodos de los objetos, y los objetos son instancias de las clases. De esta forma, se tiene una estructura jerárquica, donde las clases son los tipos de datos y los objetos son las instancias de los tipos de datos.

### Popular ORM en Python

ORM crear una capa de abstracción entre la base de datos y la aplicación, lo que permite a los desarrolladores de software trabajar con bases de datos relacionales utilizando objetos en lugar de sentencias SQL. Algunos de los ORMs más populares en Python son:

- `SQLAlchemy`: Es el más maduro y completo ORM en Python. Proporciona una API de alto nivel para trabajar con bases de datos relacionales, y soporta una amplia variedad de bases de datos, incluyendo SQLite, MySQL, PostgreSQL, Oracle, Microsoft SQL Server, y más.
- `Django ORM`: Es un ORM que viene integrado en el framework web Django. Proporciona una API de alto nivel para trabajar con bases de datos relacionales, y soporta una amplia variedad de bases de datos, incluyendo SQLite, MySQL, PostgreSQL, Oracle, Microsoft SQL Server, y más.
- `Peevee`: Es un ORM ligero y rápido para trabajar con bases de datos relacionales. Está basado sobre SQLAlchemy y el completo framework consiste de solo un fichero. Peewee provee acceso a varias bases de datos, incluyendo SQLite, MySQL, PostgreSQL, y más.
- `Storm`: Es un ORM de tamaño medio que remique a los desarrolladores escribir sentencias DDL para cada tabla en la base de datos. Soporta bases de datos como SQLite, MySQL, PostgreSQL, Oracle, y más.
- `SQLObject`: Es un ORM que mapea objetos entre DB relacionaes y Python. Gracias a su Ruby on Railes like API (Active-Objets model), se está conviertiendo rapidamente en más popular en la comunidad de desarrollo en Python. Incluye un lenguaje de consulta basado en Objetos en Python, lo que permite más abstracción sobre SQL y da independencia a las aplicaciones sobre el tipo de BD específica.

### Ventajas y Desventajas de ORM

#### Ventajas

- **Abstracción de la base de datos**: Los ORMs proporcionan una capa de abstracción entre la base de datos y la aplicación, lo que permite a los desarrolladores de software trabajar con bases de datos relacionales utilizando objetos en lugar de sentencias SQL.
- **Portabilidad**: Los ORMs permiten a los desarrolladores de software escribir código que es independiente de la base de datos subyacente, lo que facilita la portabilidad de la aplicación a diferentes bases de datos.
- **Productividad**: Los ORMs permiten a los desarrolladores de software escribir código más rápido y con menos errores, lo que aumenta la productividad y reduce el tiempo de desarrollo.

#### Desventajas

- **Complejidad**: Los ORMs pueden ser complejos de aprender y utilizar, especialmente para desarrolladores principiantes.
- **Rendimiento**: Los ORMs pueden introducir una sobrecarga de rendimiento, ya que a menudo generan sentencias SQL ineficientes.
- **Limitaciones**: Los ORMs pueden tener limitaciones en cuanto a las funcionalidades que soportan, lo que puede requerir a los desarrolladores de software escribir sentencias SQL directamente.


## PEEWEE

Peewee es un ORM ligero y rápido para trabajar con bases de datos relacionales en Python. Tiene unos pocos conceptos (pero muy expresivos), haciendolo fácil de aprender y intuitivo de usar.

Carácterísticas de Peewee:

- Un pequeño y expresivo ORM.
- Soporta SQLite, MySQL y PostgreSQL.
- Cientos de extensiones.


### Siguientes pasos

Para continuar aprendiendo sobre Peewee, lo mejor es comenzar por la documentación oficial que está en constante actualización.
[Documentación oficial de Peewee](http://docs.peewee-orm.com/en/latest/index.html)


### Ejemplo de uso










### Referencias

- [Documentación oficial de Peewee](http://docs.peewee-orm.com/en/latest/index.html)


### Ejemplos

- [Cómo hacer bases de datos con PeeWee](https://www.paradigmadigital.com/dev/como-hacer-bases-datos-con-peewee/)
- [Peewee ORM Tutorial](https://zetcode.com/python/peewee/?utm_content=cmp-true)