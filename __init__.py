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
        max_results = GetParams("maxResults")
        start_at = GetParams("startAt")
        if not session:
            session = "default"
        
        issues_in_proj = jiraSessions[session].search_issues(jql)
        arrayAux = []

        if max_results and max_results.isdigit():
            max_results = int(max_results)
            if start_at and start_at.isdigit():
                start_at = int(start_at)
            else:
                start_at = 0
            issues_in_proj = jiraSessions[session].search_issues(jql, startAt=start_at, maxResults=max_results)
        else:
            issues_in_proj = []
            startAt = 0
            maxResults = 100
            while True:
                batch = jiraSessions[session].search_issues(jql, startAt=startAt, maxResults=max_results)
                if not batch:
                    break
                issues_in_proj.extend(batch)
                startAt += len(batch)

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

    if module == "addComment":
        issueId = GetParams("issueId")
        comment = GetParams("comment")
        session = GetParams("session")
        whereToStore = GetParams("whereToStore")

        if not session:
            session = "default"
        try:
            
            jira_ = jiraSessions[session]

            jira_.add_comment(issueId, comment)

            SetVar(whereToStore, True)
        except Exception as e:
            SetVar(whereToStore, False)
            PrintException()
            raise e

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

    if module == "downloadAttachments":
        ticket_id = GetParams("id")
        session = GetParams("session")
        download_path = GetParams("path")
        whereToStore = GetParams("whereToStore")

        if not session:
            session = "default"
        issue = jiraSessions[session].issue(ticket_id)
        try:
            attachments = issue.fields.attachment
            if attachments:
                for attachment in attachments:
                    file_path = os.path.join(download_path, attachment.filename)
                    with open(file_path, 'wb') as file:
                        file.write(attachment.get())
            else:
                print("No attachments found in the ticket.")
            
            SetVar(whereToStore, True)
        except Exception as e:
            SetVar(whereToStore, False)
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e
except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e

