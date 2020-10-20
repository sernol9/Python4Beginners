from decimal import Decimal
import os
import psutil
import csv

from django.shortcuts import render


def home_view(request):
    memory = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    hdd = psutil.disk_usage('/').free / 1024 / 1024 / 1024
    csv_data = []
    with open('data.csv','r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_data.append(row)


    chart_title = 'Recycling Rate'
    chart_labels = []
    chart_data = []
    for row in csv_data:
        if row['waste_type'] == 'Plastics':
            chart_labels.append(row['year'])
            chart_data.append(row['recycling_rate'])

    ctx = {
        'memory': memory,
        'cpu': cpu,
        'hdd': hdd,
        'csv_data': csv_data,
        'chart_title': chart_title,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }

    return render(request, 'home_view.html', ctx)

def homeworks_view(request):
    card_titles = [
        'Card 1',
        'Card 2',
        'Card 3',
        'Card 4',
        'Card 5',
        'Card 6',
        'Card 7',
        'Card 8',
        'Card 9',
        'Card 10',
    ]
    data = [('2001', 1), ('2002', 3), ('2003', 2), ('2004', 5), ('2005', 2)]
    ctx = {'card_titles': card_titles, 'data': data}
    return render(request, 'homeworks_view.html', ctx)