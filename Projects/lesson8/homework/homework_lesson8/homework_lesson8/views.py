from django.shortcuts import render, redirect
from homework_lesson8.form import LoginForm

def home_view(request):
    form = LoginForm (data=request.POST)

    if request.method == 'POST':
        if form.is_valid():
            return redirect ('profile/')

    ctx = {
        'form': form,
    }

    return render (request, 'home_view.html', ctx)

def profile_view(request):
    return render (request, 'profile_view.html')