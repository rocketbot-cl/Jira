from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue

class JiraObj:

    def __init__(self):
        pass

myId = 10000

if __name__ == "__main__":
    try:
        jira = JIRA(
        # jira = JIRA(server="https://jira.atlassian.com")
        server="https://justtesting5.atlassian.net",
        basic_auth=("calebcipra@outlook.com", "oEl0pUox6GC1lxzJ0AgG166B"),  # a username/password tuple [Not recommended]
        # basic_auth=("email", "API token"),  # Jira Cloud: a username/token tuple
        # token_auth="API token",  # Self-Hosted Jira (e.g. Server): the PAT token
        # auth=("admin", "admin"),  # a username/password tuple for cookie auth [Not recommended]
        )
        projects = jira.projects()
        # print(projects)

        # Who has authenticated
        # myself = jira.myself()
        # print(myself)

        # # Create issue

        # issue_dict = {
        #     'project': {'id': 10000},
        #     'summary': 'New issue from jira-python',
        #     'description': 'Look into this one',
        #     'issuetype': {'name': 'Task'}
        # }
        # new_issue = jira.create_issue(fields=issue_dict)

        # print(new_issue)

        # # Get the mutable application properties for this server (requires
        # # jira-system-administrators permission)
        # props = jira.application_properties()

        # issues_in_proj = jira.search_issues('project=10000')
        # print(dir(issues_in_proj))
        # myissue = jira.issue('MYP-3')
        # # print(type(myissue))
        # # print(myissue.fields.summary)
        # issue_dict_to_update = {
        #     'summary': 'qweqwe'
        # }
        # myissue.update(fields=issue_dict_to_update)
        # print(myissue.fields.summary)
        # print(myissue.delete())
        # print(myissue)
        # # asd = issues_in_proj.__dir__
        # print(dir(issues_in_proj))
        # print(jira.issue('MYP-1').summary)
        
        # # summary, issue, description, asignee, tags, priority, comments
        # for each in issues_in_proj:
        #     # print(dir(each.fields))
        #     print(each.fields.summary)
        #     print(each.fields.issuetype)
        #     print(each.fields.description)
        #     print(each.fields.assignee)
        #     print(each.fields.labels)
        #     print(each.fields.priority)
        #     # print(each.fields.comment.comments)
        #     # print(dir(each.fields))
        #     # print(each.fields.comment)
        #     print(each.fields.status)
        # # issues_in_proj[0].update(status="In Progress")

        # Change status = column
        myissue = jira.issue('MYP-3')
        jira.transition_issue(myissue, transition='To Do')


    except Exception as e:
        print(e)
