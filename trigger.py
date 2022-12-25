import requests


ngrok_url = 'https://fdfa-178-80-14-106.in.ngrok.io/'
end_point = f'{ngrok_url}box-office-mojo-scraper'

r = requests.post(end_point, json={})
print(r.json()['data'])