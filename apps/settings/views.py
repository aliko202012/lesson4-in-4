from django.shortcuts import render
from apps.settings.models import Basesettings,Blog,Employees
# Create your views here.

def settings(request):
    setting = Basesettings.objects.latest('id')
    blog =Blog.objects.all().order_by("?")[:3]
    employ = Employees.objects.all().order_by("?")[:4]
    return render(request, "index.html", locals())