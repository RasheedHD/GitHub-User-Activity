import urllib.request
from urllib.error import HTTPError, URLError
import json


user = input("> ")  # Takes username from input
url = f"https://api.github.com/users/{user}/events"


def fetch_user_activity():
    try:
        resp = urllib.request.urlopen(url)
        data = resp.read()
        decodedData = data.decode("UTF-8")
        pythonList = json.loads(decodedData)
        for event in pythonList:
            if event["type"] == "PushEvent":
                print(f"- Pushed to {event["repo"]["name"]}")
            elif event["type"] == "CreateEvent":
                if event["payload"]["ref_type"] == "repository":
                    print(f"- Created repository {event["repo"]["name"]}")
                elif event["payload"]["ref_type"] == "tag":
                    print(f"- Created tag in {event["repo"]["name"]}")
                elif event["payload"]["ref_type"] == "branch":
                    print(f"- Created branch in {event["repo"]["name"]}")
            elif event["type"] == "WatchEvent":
                print(f"- Starred {event["repo"]["name"]}")
            elif event["type"] == "IssuesEvent":
                if event["payload"]["action"] == "opened":
                    print(f"- Opened a new issue in {event["repo"]["name"]}")
                elif event["payload"]["action"] == "reopened":
                    print(f"- Reopened an issue in {event["repo"]["name"]}")
                elif event["payload"]["action"] == "closed":
                    print(f"- Closed an issue in {event["repo"]["name"]}")

    except HTTPError:
        print(f"User {user} does not exist!")
    except URLError:
        print(f"URL doesn't exist!")


fetch_user_activity()
