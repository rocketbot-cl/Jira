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
import re
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
        options = {
            "server": server,
            "rest_api_version": "3"
        }
        jiraSessions[session] = JIRA(options=options, basic_auth=(email, apiToken))
        # jiraSessions[session] = JIRA(server=server, basic_auth=(email, apiToken))

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
        max_results = GetParams("max_results")
        nextToken = GetParams("nextToken")
        whereToStoreToken = GetParams("whereToStoreToken")
        custom_field=GetParams("custom_field")

        if not session:
            session = "default"
        page_size = int(max_results) if (max_results and str(max_results).isdigit()) else 50
        page_size = max(1, min(page_size, 100))
        
        
        
# Custom fields → lista
        if custom_field:
            custom_fields = [c.strip() for c in custom_field.split(",")]
        else:
            custom_fields = []

        fields_list = ["summary", "issuetype", "description", "labels", "priority", "status", "assignee", "customfield_"]
        
        
# Agregar custom fields a la petición
        for cf in custom_fields:
            if cf not in fields_list:
                fields_list.append(cf)


        try:                  
            global to_text_safe
            def to_text_safe(val):
                if val is None:
                    return None
                if isinstance(val, bytes):
                    return val.decode("utf-8", errors="replace")
                return str(val)
            global html_to_text
            def html_to_text(html):
                from html import unescape
                if not html:
                    return None
                html = to_text_safe(html)
                txt = unescape(html)
                txt = re.sub(r"<br\s*/?>", "\n", txt, flags=re.I)
                txt = re.sub(r"</p\s*>", "\n", txt, flags=re.I)
                txt = re.sub(r"<style.*?>.*?</style>", "", txt, flags=re.I | re.S)
                txt = re.sub(r"<script.*?>.*?</script>", "", txt, flags=re.I | re.S)
                txt = re.sub(r"<[^>]+>", "", txt)
                txt = txt.replace("\r\n", "\n").strip()
                txt = txt.replace("\n", " ")
                return txt or None
            
            cli = jiraSessions[session]
            resp = cli.enhanced_search_issues(
                jql_str=jql,
                nextPageToken=(nextToken if nextToken else None),
                maxResults=page_size,
                fields=fields_list,
                expand="renderedFields",
                use_post=True
            )
            
            next_token_out = getattr(resp, "nextPageToken", None)
            arrayAux = []

            try:
                import sys
                if hasattr(sys.stdout, "reconfigure"):
                    sys.stdout.reconfigure(encoding="utf-8")
            except Exception:
                pass
                
            for issue in resp or []:
                # print(issue.key)
                rendered = (issue.raw.get("renderedFields", {}) or {}).get("description")
                desc_text = html_to_text(rendered)
                if not desc_text:
                    v = getattr(issue.fields, "description", None)
                    # si viene como PropertyHolder con .raw (ADF), convierte a texto simple
                    if hasattr(v, "raw"):
                        desc_text = to_text_safe(v.raw)
                    elif isinstance(v, str):
                        desc_text = to_text_safe(v)
                    else:
                        desc_text = None
                f = {
                    "id": issue.key,  # mejor clave humana
                    "summary": to_text_safe(getattr(issue.fields, "summary", None)),
                    "issuetype": to_text_safe(getattr(issue.fields.issuetype, "name", None)),
                    "description": desc_text,
                    "labels": list(getattr(issue.fields, "labels", []) or []),
                    "priority": to_text_safe(getattr(getattr(issue.fields, "priority", None), "name", None)),
                    "status": to_text_safe(getattr(getattr(issue.fields, "status", None), "name", None)),
                    "assignee": to_text_safe(getattr(getattr(issue.fields, "assignee", None), "displayName", "Not assigned")),
                }
                
                try:
                    f['assignee'] = issue.fields.assignee.displayName
                except Exception:
                    f['assignee'] = "Not assigned"

                
                
                for cf in custom_fields:
                    value = issue.raw.get("fields", {}).get(cf)

                    if isinstance(value, list):
                        f[cf] = ", ".join([
                            str(v.get("value") or v.get("name") or v) 
                            if isinstance(v, dict) else str(v) 
                            for v in value
                        ])
                    elif isinstance(value, dict):
                        f[cf] = (
                            value.get("value")
                            or value.get("name")
                            or value.get("displayName")
                            or value.get("id")
                        )
                    else:
                        f[cf] = value

                arrayAux.append(f)


            SetVar(whereToStore, arrayAux)
            if whereToStoreToken:
                SetVar(whereToStoreToken, next_token_out)
        except Exception as e:
            SetVar(whereToStore, f"Error {e}")
            PrintException()
            import traceback
            traceback.print_exc()

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
        def text_to_adf(txt: str) -> dict:
            import re
            txt = (txt or "").replace("\r\n", "\n").strip()
            if not txt:
                # ADF no acepta vacío total: generamos un párrafo con hardBreak
                return {"type":"doc","version":1,
                        "content":[{"type":"paragraph","content":[{"type":"hardBreak"}]}]}
            paragraphs = []
            for para in re.split(r"\n\s*\n", txt):
                lines = para.split("\n")
                content = []
                for i, seg in enumerate(lines):
                    if seg:
                        content.append({"type":"text","text":seg})
                    if i < len(lines) - 1:
                        content.append({"type":"hardBreak"})
                paragraphs.append({"type":"paragraph", "content": content or [{"type":"hardBreak"}]})
            return {"type":"doc","version":1,"content":paragraphs}
        try:
            
            jira_ = jiraSessions[session]
            comment_str = str(comment).strip()
            adf = text_to_adf(comment_str)
            jira_.add_comment(issueId, adf)

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
        
        
    if module == "uploadFile":
        ticket_id = GetParams("id")
        session = GetParams("session")
        file_path = GetParams("file_path")
        whereToStore = GetParams("whereToStore")
        
        if not session:
            session = "default"
        issue = jiraSessions[session].issue(ticket_id)
        
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            with open(file_path, "rb") as file_to_upload:
                attachment = jiraSessions[session].add_attachment(
                    issue=issue, 
                    attachment=file_to_upload
                )
            if attachment:
                SetVar(whereToStore, True)

        except Exception as e:
            PrintException()
            SetVar(whereToStore, False)
                
        
except Exception as e:
    PrintException()
    raise e

