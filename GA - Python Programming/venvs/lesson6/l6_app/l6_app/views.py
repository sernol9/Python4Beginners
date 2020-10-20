from django.shortcuts import render
def home_view(request):
    return render(request, 'home_view.html')
def about_view(request):
    return render(request, 'about_view.html')
