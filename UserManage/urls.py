from django.urls import path
import UserManage.views as views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    #path('forgetpassword/', views.forgetpassword, name = 'forgetpassword'),
]