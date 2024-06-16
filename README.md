# Documentación del script.py
Este script es un programa en Python diseñado para leer datos de un archivo CSV, transformarlos en formato JSON y enviarlos a través de una solicitud HTTP a una API específica. El propósito principal de este script es automatizar el proceso de envío de datos a un servicio externo.

# Requisitos

Para ejecutar este script, se requiere tener instalado Python en el sistema. Además, se deben instalar las siguientes dependencias:

*csv* : Módulo de Python para el manejo de archivos CSV.  
*json* : Módulo de Python para la manipulación de datos en formato JSON.  
*base64*: Módulo de Python para la codificación y decodificación en Base64.  
*requests* : Librería de Python para realizar solicitudes HTTP.  

Las dependencias se pueden instalar mediante el administrador de paquetes de Python, pip, ejecutando los siguientes comandos en la línea de comandos:

```
pip install requests

```

# Uso
Descarga el archivo script.py en tu sistema.  
Abre una terminal o línea de comandos.  
Navega hasta el directorio donde se encuentra el archivo script.py.  
Ejecuta el siguiente comando para ejecutar el script:  

```
python script.py
```

El script leerá los datos del archivo CSV especificado en la variable ruta_archivo (por defecto, datos.csv). Asegúrate de que el archivo 

CSV exista en la ruta especificada y contenga los datos necesarios.

# Funcionamiento

### El script sigue los siguientes pasos para procesar los datos del archivo CSV y enviarlos a la API:

Define una función llamada leer_csv que toma la ruta de un archivo CSV como argumento.  

Abre el archivo CSV y utiliza el módulo csv para leerlo en formato de diccionario.  

### Por cada fila en el archivo CSV:

Imprime la fila leída en el formato CSV. 

Crea una lista de diccionarios que representan los datos de la fila en un formato específico.  

Convierte los datos de la fila a formato JSON utilizando la función convertir_a_json.  

Convierte el JSON a formato Base64 utilizando la función convertir_a_base64.  

Envía los datos a la API utilizando la función enviar_datos.  


### Define las funciones convertir_a_json, convertir_a_base64 y enviar_datos que realizan las siguientes tareas:

convertir_a_json: Convierte una lista de diccionarios en formato JSON utilizando el módulo json.  

convertir_a_base64: Codifica una cadena en formato JSON a Base64 utilizando el módulo base64.  

enviar_datos: Realiza una solicitud HTTP POST a una URL específica con los datos codificados en Base64  


# Personalización

### El script se puede personalizar según tus necesidades. Puedes modificar las siguientes partes:

La ruta del archivo CSV en la variable ruta_archivo.

Los campos y valores de los diccionarios en la lista datos_fila para adaptarlos a tus requisitos.

La URL de la API en la variable url dentro de la función enviar_datos.

Recuerda que cualquier modificación debe mantener la estructura y la coherencia del código para garantizar su correcto funcionamiento.



