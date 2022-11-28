from django.urls import path
import GeoFunction.views as views

urlpatterns = [
    path('QueryByBound/', views.querybybound, name = 'querybybound'),
    path('QueryByName/', views.querybyname, name = 'querybyname'),
    path('HeatMap/',views.heatmap, name = 'heatmap'),
    path('ServiceArea/',views.servicearea, name = 'servicearea'),
]