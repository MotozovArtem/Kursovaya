from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login(request):
    args={}
    args.update()
    if request.POST:
        username= request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            args['login_error']='Логин или пароль неверный'
            login_error=args['login_error']
            return render(request, 'login.html', locals())
    else:
        return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    return redirect('main')

def register(request):
    args={}
    args.update()
    args['form']=UserCreationForm()
    form=args['form']
    if request.POST:
        new_user_form=UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            newuser=auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect("main")
        else:
            args['form']=new_user_form
            form=args['form']
    return render(request, "register.html", locals())

