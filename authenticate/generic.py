from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth

from authenticate.form import UserCreationForm


class UserCreate(TemplateView):
    form = None
    template_name = "auth/auth.html"

    def get(self, request, *args, **kwargs):
        self.form = UserCreationForm()
        return super(UserCreate, self).get(request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = UserCreationForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            newuser = auth.authenticate(email=self.form.cleaned_data['email'],
                                        password=self.form.cleaned_data['password'])
            auth.login(request, newuser)
            return redirect("main")
        else:
            return super(UserCreate, self).get(request, *args, **kwargs)
