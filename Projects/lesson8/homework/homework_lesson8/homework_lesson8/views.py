from django.shortcuts import render
from homework_lesson8.form import LoginForm

def home_view(request):
    form = LoginForm (data=request.POST)

    if form.is_valid()
        return redirect ('/profile/')
    ctx = {
        'form': form,
    }
    return render(request, 'home_view.html', ctx)