from django.urls import path
import MainMap.views as views

urlpatterns = [
    path('lushanmap/', views.mainpage, name = 'lushanmap'),
    path('QueryByBound/', views.querybybound, name = 'querybybound'),
    path('QueryByName/', views.querybyname, name = 'querybyname'),
    path('HeatMap/', views.heatmap, name = 'heatmap'),
    path('ServiceArea/', views.servicearea, name = 'servicearea'),
    path('MyTrajectory/', views.mytrajectory, name = 'mytrajectory'),
    path('UploadTrajectory/', views.uploadtrajectory, name = 'uploadtrajectory'),
    path('', views.login_page, name ='login_page'),
]