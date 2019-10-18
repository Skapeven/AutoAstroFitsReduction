import requests

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print response.status_code

response2 = requests.get("http://api.open-notify.org/astros.json")
print response2.status_code
print response2.json()

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print text

jprint(response2.json())

parameters = {
    "lat": 33.45,
    "lon": -70.67
}

response3 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response3.json())

pass_times = response3.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
