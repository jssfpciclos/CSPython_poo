<!-- omit in toc -->

# Bases de Datos relacionales. Conceptos fundamentales

Un ORM (Object-Relational Mapping) es una técnica de programación que permite a los desarrolladores de software trabajar con bases de datos relacionales utilizando objetos en lugar de sentencias SQL. Un ORM mapea las tablas de una base de datos a clases de un lenguaje de programación, y las filas de las tablas a objetos de las clases.

<!-- omit in toc -->

## Indice


- [Bases de Datos relacionales. Conceptos fundamentales](#bases-de-datos-relacionales-conceptos-fundamentales)
  - [Indice](#indice)
  - [Introducción](#introducción)
    - [Modelo entidad-relación (ER)](#modelo-entidad-relación-er)
    - [Modelado y diseño de bases de datos](#modelado-y-diseño-de-bases-de-datos)
    - [Diagramas de entidad-relación (ERD)](#diagramas-de-entidad-relación-erd)
    - [Claves primarias y foráneas](#claves-primarias-y-foráneas)
    - [Tipos de relaciones. Relación uno a uno, uno a muchos y muchos a muchos](#tipos-de-relaciones-relación-uno-a-uno-uno-a-muchos-y-muchos-a-muchos)
      - [Relación uno a uno](#relación-uno-a-uno)
      - [Relación uno a muchos](#relación-uno-a-muchos)
      - [Relación muchos a muchos](#relación-muchos-a-muchos)

## Introducción

En este apartado del tema vamos a realizar un repaso a los conceptos fundamentales de las Bases de Datos relacionales.

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*kn2d699zQmsKr_Q9fdMOPw.png" width="80%">


Las entidades y las relaciones son conceptos fundamentales en el ámbito de las bases de datos. En este artículo, aprenderás qué son las entidades, las relaciones y los atributos, cómo se relacionan y en qué se diferencian, cómo se representan mediante diagramas de entidad-relación (ERD). También verás cómo se definen las claves primarias y foráneas, que permiten establecer vínculos entre las entidades, y cómo se clasifican las relaciones según su cardinalidad: uno a uno, uno a muchos y muchos a muchos. A lo largo del artículo, verás que cada concepto tiene ejemplos descritos para una mejor comprensión.

### Modelo entidad-relación (ER)

El modelo entidad-relación fue desarrollado originalmente por Peter Chen en 1976 como una técnica para modelar sistemas de información complejos de manera sencilla y comprensible.

Este modelo de entidad-relación es una técnica para diseñar modelos de datos que se utiliza para representar la estructura de una base de datos mediante entidades, atributos y relaciones.

En este modelo, una entidad representa un objeto o concepto del mundo real, como una persona, un lugar o una cosa, y los atributos describen características específicas de esa entidad. Las relaciones describen las conexiones entre entidades y especifican cómo se relacionan entre sí.

### Modelado y diseño de bases de datos

El modelado de datos permite establecer y documentar los elementos de un sistema de información mediante un gráfico conceptual. El objetivo de esto consiste en poder establecer y detallar los requisitos y la lógica del negocio en términos de estructuras de datos y relaciones entre ellos.

El diseño de base de datos, por otro lado, consiste en la creación de la misma de manera física. Esto incluye la optimización del rendimiento y la eficiencia de la base de datos, considerando aspectos como el tamaño de las bases de datos y la complejidad de las consultas, la seguridad de los datos, entre otros.

**¿Qué es una entidad?**

Con respecto a las bases de datos, una entidad es algo que existe y puede ser identificado.

Por ejemplo, una persona, un libro o un coche. Las entidades tienen atributos que las describen, como el nombre de la persona, el título del libro o el modelo del coche.

**¿Qué es una relación?**

Una relación es una conexión entre dos o más entidades en una base de datos.

Por ejemplo, una persona puede tener una relación de “compra” con un libro si esa persona ha comprado el libro. Las relaciones se utilizan para representar las interacciones o conexiones entre las entidades. Las relaciones también tienen atributos, como la fecha en que se realizó la compra.

**¿Qué son los atributos?**

Los atributos son características o propiedades que describen a una entidad o relación en una base de datos. Los atributos son la información específica que se almacena en una base de datos sobre las entidades o relaciones y están directamente relacionados con ellas para describir y diferenciar cada una de manera precisa y completa.

Por ejemplo, para una entidad “Persona”, los atributos pueden ser “nombre”, “apellido”, “edad”, “dirección”, entre otros. Para una relación “Compra”, los atributos pueden ser “fecha de compra”, “cantidad comprada”, “precio unitario”, entre otros. Los atributos permiten describir y distinguir a las entidades o relaciones en la base de datos.

**¿En qué se diferencian las entidades y las relaciones?**

La principal diferencia entre las entidades y las relaciones es que las entidades son los objetos o conceptos del mundo real que se describen en una base de datos, mientras que las relaciones son las conexiones entre esas entidades. Las entidades tienen atributos, mientras que las relaciones pueden tener atributos o no, dependiendo de la información que se quiera representar. Ambos son elementos clave en el diseño y modelado de una base de datos.

### Diagramas de entidad-relación (ERD)

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*Mpez9hp8rnpe5sgtuVS38w.jpeg" widht="80%">

Estos diagramas se utilizan para representar gráficamente las entidades, atributos y relaciones de una base de datos en un modelo conceptual, lo que permite comprender la estructura y las relaciones existentes en una base de datos.

Los diagramas de un modelo entidad-relación están compuestos por lo siguiente:

- `Entidades`: Son objetos reales sobre los cuales se desea almacenar información. Se representan utilizando rectángulos.
- `Relaciones`: Son las conexiones que existen entre los diferentes elementos del diagrama. Se representan como líneas que vinculan las entidades con los atributos.
- `Atributos`: Son las características o propiedades de una instancia en una entidad. Se representan con óvalos y se conectan a la entidad mediante líneas.
- `Cardinalidad`: Es una característica que establece la cantidad de instancias de una entidad que pueden estar relacionadas con otra entidad. Se representa en el diagrama mediante una etiqueta, que puede ser: 1:1 (uno a uno), 1:N (uno a muchos) y N:N (muchos a muchos).

Es importante tener en cuenta que existen 2 tipos de entidades:

- `Entidad fuerte`: La entidad fuerte es una entidad que existe por sí misma y no depende de ninguna otra para su existencia. A nivel gráfico, esto se representa como un rectángulo con el nombre de la entidad en su interior.
- `Entidad débil`: La entidad débil es aquella que requiere de otra entidad para existir, llamada entidad propietaria. No tiene una identidad única por sí misma. Gráficamente, se representa como un rectángulo con líneas dobles o punteadas y el nombre de la entidad en su interior.


### Claves primarias y foráneas

Estos son atributos que ayudan a establecer las relaciones entre entidades. De esta manera, una llave primaria representa un identificador único en una entidad, mientras que una llave foránea hace referencia a una llave primaria en otra entidad. Esto se representa subrayando el nombre del atributo que presenta esta característica.

La clave primaria ayuda a asegurar que no haya información duplicada en una tabla y se utiliza para vincular y relacionar datos entre tablas, mientras que la clave foránea ayuda a mantener la integridad referencial de los datos y conecta una tabla con otra.

**Ejemplo de claves primarias y foráneas**

La clave primaria se utiliza para vincular y relacionar datos entre tablas. Por ejemplo, en una base de datos de una institución educativa, la tabla de “Estudiante” puede tener una clave primaria de “Código único de matrícula”, que es un número único asignado a cada estudiante en la tabla. Luego, la tabla de “Notas” puede tener una columna llamada “Código único de matrícula” que se utiliza como una clave foránea para hacer referencia a la clave primaria de la tabla de “Estudiante”. De esta manera, se puede relacionar cada nota con el estudiante.

La clave primaria también se utiliza para garantizar la integridad de los datos. Si la clave primaria está configurada correctamente, no se puede insertar información duplicada en la tabla.

Una clave foránea funciona como un enlace entre dos tablas. Por ejemplo, si tenemos una tabla “Estudiante” y otra tabla “Notas”, podemos vincularlas mediante una clave foránea. En la tabla “Notas”, podemos incluir una columna llamada “Código único de matrícula”, que hace referencia a la clave primaria de la tabla “Estudiante”. De esta manera, podemos asegurarnos de que cada nota esté relacionada con un estudiante existente en la tabla “Estudiante”.


### Tipos de relaciones. Relación uno a uno, uno a muchos y muchos a muchos

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*o5bps-cp9Mv_8Bod50hPzQ.png" widht="80%">

Las relaciones en bases de datos permiten relacionar información entre diferentes tablas y garantizar que los datos sean precisos y consistentes.

Existen principalmente tres tipos de relaciones:

#### Relación uno a uno

Este tipo de relación entre dos tablas se establece cuando un registro de una tabla solo puede estar vinculado a un único registro en otra tabla. Este tipo de relación se utiliza generalmente para relaciones exclusivas cuando tenemos gran cantidad de campos. Dicha relación nos permite dividir la información en tablas más pequeñas con menos cantidad de campos y facilitar la gestión de nuestras bases de datos.

Dicha relación se establece a través de una Foreign Key que se vincula directamente con la Primary Key de la tabla principal. En este tipo de relaciones será indistinto que tabla considerar principal y que tabla dependiente para establecer la Foreign Key, siendo ello decisión de diseño del administrador de acuerdo a los datos que guardar en las tablas.

<img src="https://sqlearning.com/es/introduccion-sql-server/relaciones/relacion-1a1.png" widht="50%">

#### Relación uno a muchos

Significa que una fila en una tabla está relacionada con varias filas en otra tabla. Esta relación se utiliza a menudo cuando hay una entidad principal que tiene varios registros relacionados en otra tabla. Por ejemplo, si tenemos una tabla de “Estudiantes” y una tabla de “Asignaturas”, cada estudiante puede tener varias asignaturas, lo que significa que la relación entre las dos tablas es de uno a muchos.

<img src="https://sqlearning.com/es/introduccion-sql-server/relaciones/relacion-1aN.png" widht="50%">

#### Relación muchos a muchos

Significa que muchas filas en una tabla están relacionadas con muchas filas en otra tabla. Este tipo de relación se utiliza a menudo cuando hay una entidad que tiene una relación compleja con otra entidad. Por ejemplo, si tenemos una tabla de “Estudiantes” y una tabla de “Cursos”, donde cada estudiante puede tomar varios cursos y cada curso puede tener varios estudiantes, la relación entre las dos tablas sería muchos a muchos. Para implementar esta relación, se utiliza una tabla intermedia, también conocida como tabla de “unión” o tabla “puente”.

Usualmente la Primary Key de la tercera tabla intermedia será una clave Compuesta o Composite key de las Primary Key de las dos tablas principales y a través de dichas claves formará dos Foreign Key a cada tabla con la que establece relación. Además, esta tercera tabla aparte de establecer las relaciones intermedias, también podrá guardar información adicional como por ejemplo información de auditoría u otros datos importantes del establecimiento de la relación.


<img src="https://sqlearning.com/es/introduccion-sql-server/relaciones/relacion-NaN.png" widht="50%">


Cada tipo de relación tiene su propio propósito y ventajas, y es importante elegir la relación correcta para garantizar la eficiencia de la base de datos.

