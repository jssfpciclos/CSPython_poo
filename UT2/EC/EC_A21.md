## UT2. Ejercicios Ficheros. Trabajo con sistemas de ficheros

### Ejercicio 1

Escribe un programa en Python que normalice una ruta de archivo. El programa debe pedir al usuario que ingrese una ruta de archivo y luego mostrar la ruta normalizada.

**Instrucciones:**
Pide al usuario que ingrese una ruta de archivo (puede ser absoluta o relativa).
Utiliza la función adecuada de la biblioteca os.path para normalizar la ruta.
Muestra la ruta original y la ruta normalizada en la salida.

```python
import os

def normalizar_ruta():
    # Pide al usuario que ingrese una ruta de archivo
    ruta_original = input("Ingresa una ruta de archivo: ")

    # Normaliza la ruta utilizando os.path.normpath()
    ruta_normalizada = os.path.normpath(ruta_original)

    # Muestra la ruta original y la ruta normalizada
    print("\nRuta Original:", ruta_original)
    print("Ruta Normalizada:", ruta_normalizada)

# Llama a la función para ejecutar el programa
normalizar_ruta()
```

### Ejercicio 2

Escribe un script en Python que muestre el contenido de un directorio y sus subdirectorios hasta un límite, indicado como parámetro a través de un parámetro.
El script debe utilizar la función os.scandir() para obtener el contenido y utilizar recursividad para mostrar el contenido de los subdirectorios.

La información que se debe mostrar por cada elemento del directorio es:
- Nombre del elemento | Tipo de elemento (fichero o directorio) | Tamaño del elemento (en bytes) | Fecha de modificación (en formato legible)


**Instrucciones:**

1. La función main debe obtener los siguientes parámeros de argumentos:
   - La ruta del directorio a mostrar
   - El límite de recursividad
   - Si se muestra en forma de arbol, o en detalle. (opcional), por defecto en detalle.
  
  En caso de no proporcionarse, el programa debe mostrar un mensaje de error y terminar).
   
2. Si se muestra en formato arbol, será así:
```
|-- directorio1
|   |-- subdirectorio1
|   |   |-- archivo1
|   |   |-- archivo2
|   |-- archivo3
|-- archivo4
```

3. Si se muestra en formato detalle, será así:
```
directorio:
archivo1 | 1234 bytes | 2021-01-01 12:00:00
archivo2 | 1234 bytes | 2021-01-01 12:00:00
archivo4 | 1234 bytes | 2021-01-01 12:00:00

  sub_dir_1
  archivo3 | 1234 bytes | 2021-01-01 12:00:00

  sub_dir_2
  archivo5 | 1234 bytes | 2021-01-01 12:00:00
```
  

> 😎 **Pista**<br>
> Leer los argumentos de la línea de comandos con el módulo sys. `sys.argv` es una lista que contiene los argumentos pasados al script desde la línea de comandos.
> Convertir UnixEpoch a fecha legible con `datetime.datetime.fromtimestamp(342342342)`
> Para pasar los `bytes` a `KB` o `MB` se puede utilizar la función `convertir_bytes` que se muestra a continuación.



```python
import os

def convertir_bytes(bytes):
    # Función para convertir bytes a KB o MB
    KB = 1024
    MB = 1024 * KB

    if bytes >= MB:
        return f"{bytes/MB:.2f} MB"
    elif bytes >= KB:
        return f"{bytes/KB:.2f} KB"
    else:
        return f"{bytes} bytes"
```
