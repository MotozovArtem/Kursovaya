from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def login(request):
    args = {}
    args.update()
    if request.POST:
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            args['login_error'] = 'Логин или пароль неверный'
            login_error = args['login_error']
            return render(request, 'auth/login.html', locals())
    else:
        return render(request, 'auth/login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('main')
