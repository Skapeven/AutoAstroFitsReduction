import requests

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print response.status_code

