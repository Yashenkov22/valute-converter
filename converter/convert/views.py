from django.shortcuts import render
import requests

def index(request):
    response = requests.get(url='https://www.cbr-xml-daily.ru/daily_json.js').json()
    # list_valute = [response['Valute'][i]['Name'] for i in response['Valute'].keys()]
    # list_valute = response['Valute'].keys()
    list_name = sorted([' '.join((i, response['Valute'][i]['Name'])) for i in response['Valute'].keys()], key=lambda x: x[0])


    if request.method == 'GET':
        context = {
            'list_name' : list_name,
        }
        return render(request, 'convert/index.html', context)
    
    if request.method == 'POST':
        from_amount = float(request.POST.get('amount'))
        from_cur = request.POST.get('from_curr').split()[0]
        to_cur = request.POST.get('to_curr').split()[0]
        frm = response['Valute'][from_cur]['Value']
        t = response['Valute'][to_cur]['Value']
        converted_amount = round(((frm / t) * from_amount), 2)

        context = {
            'from_amount' : from_amount,
            'from_curr' : request.POST.get('from_curr'),
            'to_curr' : request.POST.get('to_curr'),
            'list_name' : list_name,
            'result' : converted_amount
        }
        
        return render(request, 'convert/index.html', context)