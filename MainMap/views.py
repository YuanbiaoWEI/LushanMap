from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from MainMap import models


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

@login_required
def heatmap(request):
    return render(request, "Map/HeatMap.html")

@login_required
def servicearea(request):
    return render(request, "Map/ServiceArea.html")

@login_required
def mytrajectory(request):
    return render(request, "Trajectory/MyTrajectory.html")

@login_required
def uploadtrajectory(request):
    return render(request, "Trajectory/UploadTrajectory.html")

@login_required
def deletetrajectory(request):
    trajectorylist = []
    SQL = models.SQLSearchTrajectoryByUsername(request.user.username)
    result = models.execSQL(SQL)
    for eachtrajectory in result:
        trajectorylist.append(eachtrajectory)
    context = {
        'trajectorylist':trajectorylist
    }

    return render(request, "Trajectory/DeleteTrajectory.html",context)