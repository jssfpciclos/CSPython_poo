# Ejemplos trabajo con Peewee


## Select en Peewee

En este artículo se describen algunas maneras y ejemplos para hacer select en peewee, esta sintaxis de uso se puede usar con cualquier manejador de base de datos al que esté configurado peewee.

Imaginando que se tiene un modelo parecido al siguiente:

```python
class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    id = AutoField()
    name = CharField(max_length=1024)
    email = CharField(max_length=1024)

db.create_tables([Users], safe=True)
```

Esto se va a almacenar en un fichero llamado `models.py` y se va a importar en el fichero donde se va a hacer el select.

### Seleccionar un registro simple

```python
from peewee import *
from . import models

users = models.Users
id = 8
user = users.select().where(users.id == id)
```

Trayendo específicamente los campos sería:

```python
from peewee import *
from . import models

users = models.Users
id = 8

user = users.select(users.email, users.name).where(users.id == id)
```

Con la sintaxis de peewee la manera más sencilla sería:

```python
users = models.Users
id = 8
user = users.get(users.id == id)
```

De esta manera se obtiene el objeto del registro, dicho registro se puede desmenuzar como el siguiente ejemplo:

```python
print (user.name)
print (user.id)
```

En caso de evitar excepciones de no existir el registro, se puede usar la siguiente sintaxis:

```python
user = users.get_or_none(users.id == id)
```

De esta manera se puede discriminar si el resultado es distinto de None.

También se puede utilizar los siguientes métodos para obtener un solo registro:

```python
user = users.get_by_id(id)  # Si no existe lanza una excepción
user = users.get_or_create(users.id == id)  # Si no existe lo crea
```

También es posible obtener el primer registro de una tabla con la siguiente sintaxis:

```python
user = users.select().first()
```




### Seleccionar múltiples registros

Seleccionar múltiples registros pudiera ser obteniendo todos los registros de una tabla de la siguiente manera:

```python
from peewee import *
from . import models

users = models.Users
list_users = users.select()
```

De esta manera se debería recorrer el resultado como una lista:

```python
for user in list_users:
    print (user.name)
    print (user.id)
```

También se pueden obtener los registros haciendo un select orientado a un criterio específico, por ejemplo:

```python
from peewee import *
from . import models

users = models.Users
list_users = users.select().where(users.name == 'nuxpy')
```

Donde coincida el criterio traerá todos los registros y se visualizarán como una lista igual que el caso anterior. En estos criterios también se pueden realizar búsquedas con expresiones regulares, por ejemplo:

```python
from peewee import *
from . import models

users = models.Users
src = '.*nuxpy.*'
list_users = users.select().where(users.name.iregexp(r'%s' % src))
```


### Seleccionar y ordenar salida de registros

También se pueden ordenar los resultados de estas consultas, tanto de manera ascendente como de manera descendente, el ejemplo más básico sería:

```python
users = models.Users
list_users = users.select().where(users.name == 'nuxpy').order_by(users.id)
```
Definiendo de manera ascendente o descendente sería:

```python
users = models.Users
list_users_desc = users.select().where(users.name == 'nuxpy').order_by(users.id.desc()) # Descendente
list_users_asc = users.select().where(users.name == 'nuxpy').order_by(users.id.asc()) # Ascendente
```


### Select compuestos en peewee

**Select con fn y alias.**

En donde el tipo de dato date = DateField() puede "apartar" las referencias de: año - mes - día; en variables respectivas, pudiendo crear para dichas referencias en su respectivos alias.

Igualmente podemos usar el recurso fn.Count para contar el número de resultados:

```python	
from peewee import *
from . import models

users = models.Users

query = (users
         .select(
             fn.Count(users.id).alias('total'),
             fn.DatePart('year', users.date).alias('year'),
             fn.DatePart('month', users.date).alias('month'),
             fn.DatePart('day', users.date).alias('day'))

         .group_by(fn.DatePart('year', users.date),
                    fn.DatePart('month', users.date),
                    fn.DatePart('day', users.date))
         .order_by(fn.DatePart('year', users.date),
                   fn.DatePart('month', users.date),
                   fn.DatePart('day', users.date)))
```

**Select con join**

En este ejemplo se puede visualizar un join uniendo dos tablas, a su vez creando alias:

```python	
from peewee import *
from . import models

users = models.Users
orders = models.Orders

query = (users
         .select(users, orders)
         .join(orders, on=(users.id == orders.user_id))
         .where(users.name == 'nuxpy'))
```
También es posible obviar los IDs de ambas tablas, ya que se puede hacer referencia a ellos de la siguiente manera:

```python
query = (users
         .select(users, orders)
         .join(orders, on=(users == orders.user))
         .where(users.name == 'nuxpy'))
```

o incluso se puede omitir la cláusula `on`:

```python	
query = (users
         .select(users, orders)
         .join(orders)
         .where(users.name == 'nuxpy'))
```

ya que peewee automáticamente detecta las claves foráneas y las utiliza para hacer el join.

**Select con subquery**

En este ejemplo se puede visualizar un subquery, en donde se puede hacer una consulta a una tabla y a su vez hacer una consulta a otra tabla:

```python
from peewee import *
from . import models

users = models.Users
orders = models.Orders

subquery = (orders
            .select(fn.Count(orders.id).alias('total'))
            .where(orders.user == users))

query = (users
          .select(users, subquery.alias('orders'))
          .where(users.name == 'nuxpy'))
```

Esto haría una query SQL como la siguiente:

```sql
SELECT "t1"."id", "t1"."name", "t1"."email", 
  (SELECT COUNT("t2"."id") AS "total" FROM "orders" AS "t2" WHERE ("t2"."user_id" = "t1"."id")) AS "orders" 

FROM "users" AS "t1" WHERE ("t1"."name" = 'nuxpy')
```

**Select con operadores Or y And**

En este ejemplo se puede visualizar un select con operadores Or y And, en donde se puede hacer una consulta a una tabla y a su vez hacer una consulta a otra tabla:

```python
from peewee import *
from . import models

user = models.Users
tweet = models.Tweets

tweet.select().join(user)
  .where((User.is_staff == True) | (User.is_superuser == True))


Para más ejemplos consultar la [documentación de peewee, Querying](https://docs.peewee-orm.com/en/latest/peewee/querying.html#). 
```