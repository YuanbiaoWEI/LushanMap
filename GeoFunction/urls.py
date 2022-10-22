from django.urls import path
import GeoFunction.views as views

urlpatterns = [
    path('QueryByBound/', views.querybybound, name = 'querybybound'),
    path('QueryByName/', views.querybyname, name = 'querybyname'),
    #path('login/', views.login, name = 'login'),
    #path('logout/', views.logout, name = 'logout'),
    #path('forgetpassword/', views.forgetpassword, name = 'forgetpassword'),
]