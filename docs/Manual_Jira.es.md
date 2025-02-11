



# Jira
  
Interactúa con el ecosistema de Jira.  

*Read this in other languages: [English](Manual_Jira.md), [Português](Manual_Jira.pr.md), [Español](Manual_Jira.es.md)*
  
![banner](imgs/Banner_Jira.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

Para usar este modulo se requiere una cuenta con Jira y activar un API Token (Perfil -> Opciones de cuenta -> Seguridad -> API Token).


## Descripción de los comandos

### Conectar a Jira
  
Conectar tu cuenta de Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Servidor|Servidor en la que se encuentran nuestros proyectos|https://myserver.atlassian.net|
|Email|Mail registrado en el proyecto|ejemplo@rocketbot.com|
|API Token|Token obtenido desde Jira|oEl0pUox6GC1lxzJ0AgGPRos|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Obtener proyectos
  
Obtiene la lista de proyectos de Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Obtener tickets
  
Obtiene la lista de tickets de Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtros (en formato JQL)|Query con filtros|project=PROJ|
|Número de resultados|Maximo numero de tickets a obtener. Por defecto trae todos.|all|
|Empezar desde|Número de ticket desde el cual empezar a obtener los resultados. Útil para paginar. Ej si startAt = 100 y maxResults = 50, se obtendrán los tickets del 101 al 150|0|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Crear un ticket
  
Crea un ticket en Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Diccionario con valores del ticket|Diccionario con los valores que requiere el ticket|{'project' : {'id' : 10000}, 'summary': 'titulo del ticket', 'issuetype':'Task'}|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Mover un ticket
  
Mueve un ticket desde una columna a otra
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del ticket que se desea mover|Id del ticket a mover|MYP-1|
|Columna a la que se desea mover|Columna en la cual se requiere el ticket|In Progress|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Editar un ticket
  
Permite editar un ticket en Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del ticket que se desea editar|Id del ticket a editar|MYP-1|
|Diccionario con valores del ticket|Diccionario con los valores que se requiere cambiar en el ticket|{'summary': 'titulo del ticket'}|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Añadir comentario a un ticket
  
Permite añadir un comentario a un ticket en Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del ticket a comentar|Id del ticket al que se le quiere añadir un comentario|MYP-1|
|Sesion|Nombre de la sesion|conn1|
|Comentario|Comentario a añadir al ticket|Este es un comentario|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Eliminar un ticket
  
Permite eliminar un ticket en Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del ticket que se desea eliminar|Id del ticket a borrar|MYP-1|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Obtener transiciones
  
Obtiene la lista de transiciones disponibles de un ticket de Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del ticket que se saber las transiciones|Id del ticket a examinar las transiciones|MYP-1|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|

### Descargar adjuntos
  
Descarga los archivos adjuntos de un ticket de Jira
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del ticket|Id del ticket a descargar los archivos adjuntos|MYP-1|
|Ruta de descarga|Ruta donde se descargarán los archivos adjuntos|/Users/user/Desktop|
|Sesion|Nombre de la sesion|conn1|
|Asignar resultado a variable|Variable donde guardar el resultado|Variable|
