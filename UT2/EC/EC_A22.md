## UT2. A22. Ejercicios Ficheros

### Ejercicio 1

Escribe una función `ContarPalabrasLineas` la cual cuente el número de líneas y el número de palabras dentro del fichero.

La función debe retornar un diccionario:

```python
{
    "lineas": 0,
    "palabras": 0
}
```

> Las palabras se considerarán separadas por espacios.


### Ejercicio 2

El siguiente [fichero](https://github.com/rameshovyas/30-Days-of-Python-Exercises/blob/main/Day_19_File_Handling/Level2/email_exchanges_big.txt) contiene una serie de información sobre correos electrónicos.

Extrae todas las direcciones de emails de las cuales se han recibido correos electrónicos.

El método debe retornar una lista con todas las direcciones de email.

```python	
def extract_incoming_emails_address(fichero: str) -> list:
    pass
```

> Nota: Las direcciones están en las líneas que comienza con `From`.


### Ejercicio 3

Crea una función `PalabrasMasFrecuentes` que devuelva una lista con las palabras más frecuentes en el fichero.

Utilizar para ello cualquier fichero de texto, que se pase como parámetro.

```python	
def PalabrasMasFrecuentes(fichero: str, TopN: int) -> list[str]:
    pass
```

> 📄 Nota:<br> 
> - Las palabras se considerarán separadas por espacios.
> - Ordenar un diccionario por valor: `sorted(diccionario.items(), key=lambda x: x[1], reverse=True)`