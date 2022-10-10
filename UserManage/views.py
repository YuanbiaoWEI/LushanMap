from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup(request):
    state = None
    password = request.POST.get('passwprd','')
    repeat_password = request.POST.get('repeat_passwprd','')
    if password != repeat_password:
        state = 'repeat_error'
    else:
        username = request.POST.get('username','')
        if User.objects.filter(username=username):
            state = 'user_exist'
        else:
            userinfo = {'username':username,'password':password,'email':request.POST.get('email','')}
            new_user = User.objects.create_user(**userinfo)
            new_user.save()
            state = 'success'
    response = {'state': state, 'User': None}
    return JsonResponse(response)

@csrf_exempt
def login(request):
    state = None
    password = request.POST.get('password', '')
    username = request.POST.get('username', '')
    print('password:',password,'username:',username)
    user = auth.authenticate(username=username,password=password)
    print('user:',user)
    if user is not None:
        auth.login(request, user)
        state = 'success'
    else:
        state = 'not_exist_or_password_error'
    response = {'state': state, 'User': None}
    return JsonResponse(response)