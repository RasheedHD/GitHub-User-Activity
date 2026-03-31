import urllib.request
import json

user = input("> ")
url = f"https://api.github.com/users/{user}/events"

def fetch_user_activity():
    resp = urllib.request.urlopen(url)
    data = resp.read()
    decodedData = data.decode("UTF-8")
    pythonList = json.loads(decodedData)
    #print(pythonList)
    for event in pythonList:
        if event["type"] == "PushEvent":
            print(f"- Pushed 1 commit to {event["repo"]["name"]}")
            pass
        elif event["type"] == "CreateEvent":
            print(f"- Created repository {event["repo"]["name"]}")
        elif event["type"] == "WatchEvent":
            print(f"- Starred {event["repo"]["name"]}")


fetch_user_activity()