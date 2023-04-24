import requests

response = requests.get(url='https://www.cbr-xml-daily.ru/daily_json.js').json()

print(response['Valute'])
print([response['Valute'][i]['Name'] for i in response['Valute'].keys()])


