



# Jira
  
Interaja com o ecossistema Jira.  

*Read this in other languages: [English](Manual_Jira.md), [Português](Manual_Jira.pr.md), [Español](Manual_Jira.es.md)*
  
![banner](imgs/Banner_Jira.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  




## Como usar este modulo

Para usar esse módulo, você precisa ter uma conta no Jira e ativar um token de API (Profile -> Account Options -> Security -> API Token).
## Descrição do comando

### Conectar-se ao Jira
  
Conecte sua conta do Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Servidor|Servidor em que nossos projetos estão hospedados|https://myserver.atlassian.net|
|Email|E-mail registrado no projeto|example@rocketbot.com|
|API Token|Token obtido do Jira|oEl0pUox6GC1lxzJ0AgGPRos|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado à variável|Variável onde armazenar o resultado|Variável|

### Obter projetos
  
Obtém a lista de projetos do Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Nome da sessão|conn1|
|Atribuir resultado à variável|Variável onde armazenar o resultado|Variável|

### Obter tickets
  
Obtém a lista de tickets do Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtros (em formato JQL)|Consulta com filtros|project=PROJ|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado à variável|Variável onde armazenar o resultado|Variável|

### Criar um ticket
  
Cria um ticket no Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dicionário com valores do ticket|Dicionário com os valores que o ticket requer|{'project' : {'id' : 10000}, 'summary': 'título do ticket', 'issuetype':'Task'}|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado a variável|Variável onde guardar o resultado|Variável|

### Mover um ticket
  
Move um ticket de uma coluna para outra
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do ticket que se deseja mover|Id do ticket a mover|MYP-1|
|Coluna para a qual deseja movê-lo|Coluna na qual o ticket é necessário|In Progress|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado a variável|Variável onde armazenar o resultado|Variável|

### Editar um ticket
  
Permite editar um ticket em Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do ticket que se deseja editar|Id do ticket a editar|MYP-1|
|Dicionário com valores do ticket|Dicionário com os valores que se requer mudar no ticket|{'summary': 'titulo do ticket'}|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado a variável|Variável onde guardar o resultado|Variável|

### Adicionar comentário a um ticket
  
Permite adicionar um comentário a um ticket no Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do ticket a comentar|Id do ticket ao qual você deseja adicionar um comentário|MYP-1|
|Sessão|Nome da sessão|conn1|
|Comentário|Comentário a adicionar ao ticket|Este é um comentário|
|Atribuir resultado a variável|Variável onde armazenar o resultado|Variável|

### Eliminar um ticket
  
Permite eliminar um ticket em Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do ticket que deseja eliminar|Id do ticket a eliminar|MYP-1|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado a variável|Variável onde guardar o resultado|Variável|

### Obter transições
  
Obtém a lista de transições disponíveis de um ticket de Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do ticket que se saber as transições|Id do ticket a examinar as transições|MYP-1|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado a variável|Variável onde guardar o resultado|Variável|

### Download attachments
  
Download the attachments de um ticket de Jira
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Id do ticket|Id do ticket a baixar os arquivos adjuntos|MYP-1|
|Caminho de download|Caminho onde os arquivos adjuntos serão baixados|/Users/user/Desktop|
|Sessão|Nome da sessão|conn1|
|Atribuir resultado a variável|Variável onde guardar o resultado|Variável|
