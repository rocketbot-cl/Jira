# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Jira' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue

global jiraSessions

SESSION_DEFAULT = "default"
try:
    if not jiraSessions :
        jiraSessions = {SESSION_DEFAULT:{}}
except NameError:
    jiraSessions = {SESSION_DEFAULT:{}}

module = GetParams("module")

try:
    if module == "connectToJira":
        server = GetParams("server")
        email = GetParams("email")
        apiToken = GetParams("apiToken")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")
        resultConnection = False
        if not session:
            session = "default"

        jiraSessions[session] = JIRA(server=server, basic_auth=(email, apiToken))
        if jiraSessions[session]:
            resultConnection = True
        
        SetVar(whereToStore, resultConnection)

    if module == "obtainProjects":
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")

        if not session:
            session = "default"

        myProjects = jiraSessions[session].projects()
        arrayAux = []
        # print(myProjects)
        for each in myProjects:
            f = {
                'id': each.id,
                'key': each.key,
                'name': each.name
            }
            arrayAux.append(f)

        SetVar(whereToStore, arrayAux)

    if module == "obtainTickets":
        jql = GetParams("jql")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")

        if not session:
            session = "default"
        
        issues_in_proj = jiraSessions[session].search_issues(jql)

        arrayAux = []

        print(issues_in_proj)
        for issue in issues_in_proj:
            print(issue.__str__())
            f = {
                'id': issue.__str__(),
                'summary': issue.fields.summary,
                'issuetype': issue.fields.issuetype.name,
                'description': issue.fields.description,
                'labels': issue.fields.labels,
                'priority': issue.fields.priority.name,
                'status': issue.fields.status.name
            }
            try:
                f['assignee'] = issue.fields.assignee.displayName
            except:
                f['assignee'] = "Not assigned"
            arrayAux.append(f)

        SetVar(whereToStore, arrayAux)

    if module == "moveTicket":
        issueId = GetParams("issueId")
        transitionTo = GetParams("transitionTo")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")

        if not session:
            session = "default"

        issueMoved = False
        myIssue = jiraSessions[session].issue(issueId)
        jiraSessions[session].transition_issue(myIssue, transition=transitionTo)
        myIssueVerification = jiraSessions[session].issue(issueId)
        if myIssueVerification.fields.status.name == transitionTo:
            issueMoved = True

        SetVar(whereToStore, issueMoved)

    if module == "createTicket":
        issueDict = GetParams("issueDict")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")
        
        try:
            issueDict = eval(issueDict)
        except:
            pass

        if not session:
            session = "default"

        newIssue = jiraSessions[session].create_issue(fields=issueDict)
        
        SetVar(whereToStore, newIssue)

    if module == "updateTicket":
        issueId = GetParams("issueId")
        issueDict = GetParams("issueDict")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")

        try:
            issueDict = eval(issueDict)
        except:
            pass

        if not session:
            session = "default"

        issue = jiraSessions[session].issue(issueId)

        issueUpdated = issue.update(fields=issueDict)

        SetVar(whereToStore, True)

    if module == "deleteTicket":
        issueId = GetParams("issueId")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")

        if not session:
            session = "default"

        issue = jiraSessions[session].issue(issueId)
        issueDeleted = issue.delete()

        SetVar(whereToStore, True)

    if module == "obtainTransitions":
        issueId = GetParams("issueId")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")

        if not session:
            session = "default"

        issue = jiraSessions[session].issue(issueId)
        transitions = jiraSessions[session].transitions(issue)
        arrayAux = []
        for t in transitions:
            print(t)
            f = {
                "id": t["id"],
                "name": t["name"],
                "name in sight": t["to"]["name"]
            }
            arrayAux.append(f)

        SetVar(whereToStore, arrayAux)

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e

