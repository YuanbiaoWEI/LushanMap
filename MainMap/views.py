from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def mainpage(request):
    context = {'user': request.user }
    return render(request, "Map/LushanMap.html", context)

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/lushanmap/')
    return render(request, "User/Login.html")

@login_required
def querybybound(request):
    return render(request, "Map/QueryByBound.html")

@login_required
def querybyname(request):
    return render(request, "Map/QueryByName.html")