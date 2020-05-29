from django.shortcuts import render
import requests
from decimal import Decimal
from .forms import MyForm

def home_view(request):
    response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=96e66346-68bb-4ca9-b001-58bbf39e36a7")
    dict = response.json()
    years = []
    found = False
    form = MyForm()

    for i in dict['result']['records']:
        j = 0
        while not found and j < len(years):
            found = ( True if years[j][0] == i['month'][0:4] else False)
            j+=1
        if found:
            if years[j-1][1] < Decimal(i['max_temperature']):
                years[j-1][1] = Decimal(i['max_temperature'])
            found = False
        else:
            years += [[i['month'][0:4],Decimal(i['max_temperature'])]]
    lista = sorted(years)

    if 'from_year' in request.GET and 'to_year' in request.GET:
        form = MyForm(request.GET)
        form.min_max(lista[0][0],lista[len(lista)-1][0])
        if form.is_valid():
            index = 0
            while index < len(lista) and int(lista[index][0]) <= form.cleaned_data.get('to_year'):
                if (int(lista[index][0]) < form.cleaned_data.get('from_year')):
                    del lista[index]
                    index -= 1
                index += 1
            lista = lista[:index]
    else:
        form = MyForm()

       
    ctx = {
        'data' : lista,
        'form' : form
    }
    return render (request, 'home_view.html',ctx)


