



# Jira

Interactúa con el ecosistema de Jira. Puedes crear, leer, modificar y eliminar tickets, moverlos hacia las columnas que necesites, todo a tu voluntad.
  
![banner](imgs/Banner_Jira.jpg)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  


## Como usar este modulo
Para usar este modulo se requiere una cuenta con Jira y activar un API Token (Perfil -> Opciones de cuenta ->
Seguridad -> API Token).


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

### Elimiar un ticket
  
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
