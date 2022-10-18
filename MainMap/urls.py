from django.urls import path
import MainMap.views as views

urlpatterns = [
    path('lushanmap/', views.mainpage, name = 'lushanmap'),
    path('QueryByBound/', views.querybybound, name = 'querybybound'),
    path('QueryByName/', views.querybyname, name = 'querybyname'),
    path('', views.login_page, name ='login_page'),
]