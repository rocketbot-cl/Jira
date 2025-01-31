



# Jira
  
Interact with the Jira's ecosystem.  

*Read this in other languages: [English](Manual_Jira.md), [Português](Manual_Jira.pr.md), [Español](Manual_Jira.es.md)*
  
![banner](imgs/Banner_Jira.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

In order to use this module you need a Jira's account and an API Token (Profile -> Account options -> Security -> API Token).


## Description of the commands

### Connects to Jira
  
Enable the conection to Jira
|Parameters|Description|example|
| --- | --- | --- |
|Server|Server which our projects are hosted|https://myserver.atlassian.net|
|Email|Mail registered in the project|example@rocketbot.com|
|API Token|Token obtained from Jira|oEl0pUox6GC1lxzJ0AgGPRos|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Obtain projects
  
Obtains the list of projects from Jira
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Obtain tickets
  
Obtains the list of tickets from Jira
|Parameters|Description|example|
| --- | --- | --- |
|Filters (in JQL format)|Query with filters|project=PROJ|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Create a ticket
  
Creates a ticket in Jira
|Parameters|Description|example|
| --- | --- | --- |
|Dictionary with parameters of the ticket|Dictionary with values that the ticket needs|{'project' : {'id' : 10000}, 'summary': 'title of the ticket', 'issuetype':'Task'}|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Move a ticket
  
Moves a ticket from one column to another
|Parameters|Description|example|
| --- | --- | --- |
|Id of the ticket to move|Id if the ticket to change its column|MYP-1|
|Column where to move it|Column in which the thicket is requiered|In Progress|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Update a ticket
  
Allows you to update a ticket in Jira
|Parameters|Description|example|
| --- | --- | --- |
|Id of the ticket to edit|Id if the ticket to change its values|MYP-1|
|Dictionary with parameters of the ticket|Dictionary with values that the ticket needs to change|{'summary': 'title of the ticket'}|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Add comment to a ticket
  
Allows to add a comment to a ticket in Jira
|Parameters|Description|example|
| --- | --- | --- |
|Id of the ticket to comment|Id of the ticket to which you want to add a comment|MYP-1|
|Session|Name of the session|conn1|
|Comment|Comment to add to the ticket|This is a comment|
|Assign result to variable|Variable where to store the result|Variable|

### Delete a ticket
  
Allows you to delete a ticket in Jira
|Parameters|Description|example|
| --- | --- | --- |
|Id of the ticket to delete|Id if the ticket to erase|MYP-1|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Obtain transitions
  
Obtains the list of transitions availables of a ticket from Jira
|Parameters|Description|example|
| --- | --- | --- |
|Id of the ticket to know its transitions|Id if the ticket to examine for transitions|MYP-1|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|

### Download attachments
  
Download the attachments of a ticket from Jira
|Parameters|Description|example|
| --- | --- | --- |
|Id of the ticket|Id of the ticket to download the attachments|MYP-1|
|Download path|Path where the attachments will be downloaded|/Users/user/Desktop|
|Session|Name of the session|conn1|
|Assign result to variable|Variable where to store the result|Variable|
