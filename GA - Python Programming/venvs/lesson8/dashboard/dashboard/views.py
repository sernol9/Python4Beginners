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
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_data.append(row)


    chart_title = 'Recycling Rate'
    chart_labels = []
    chart_data = []
    waste_type = request.GET.get('waste_type', 'Plastics')
    for row in csv_data:
        if row['waste_type'] == waste_type:
            chart_labels.append(row['year'])
            chart_data.append(row['recycling_rate'])

 # new code
    from datetime import datetime
    filename = request.POST.get('filename')
    change_time = None
    if filename:
        change_time = datetime.fromtimestamp(os.path.getmtime(filename))

    ctx = {
        'filename': filename,
        'change_time': change_time,
        # end of new code
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

def blog_view(request, year, month, day, slug):
    ctx = {
        'year': year,
        'month': month,
        'day': day,
        'slug': slug,
    }
    return render(request, 'blog_view.html', ctx)
    
from .forms import MyForm
def form_view(request):
    print(request.POST)

    form = MyForm()

    if request.method == 'POST':
        form = MyForm(data=request.POST)
        form.is_valid()

    ctx = {'form': form}

    return render(request, 'form_view.html', ctx)

