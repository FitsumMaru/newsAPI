import requests

from coindesk.client import CoindeskAPIClient
api_client = CoindeskAPIClient.start('currentprice')
response = api_client.get()

url = 'https//jsonplaceholder.typicode.com/posts'
data = {'title', 'Special Agent', 'body: Leroy Jet'}

Response = requests.post(url, data)
print(response.status_code)
print(response.json())
