from django.shortcuts import render

# Create your views here.

def lichn_kab(request):
    return render(request, "lichn_kab.html", locals())