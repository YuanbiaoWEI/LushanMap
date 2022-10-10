from django.urls import path
import MainMap.views as views

urlpatterns = [
    path('lushanmap/', views.mainpage, name = 'lushanmap'),
    path('', views.login_page, name ='login_page'),
]