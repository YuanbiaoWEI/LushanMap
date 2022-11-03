from django.urls import path
import TrajectoryManage.views as views

urlpatterns = [
    path('MyTrajectory/',views.mytrajectory, name = 'mytrajectory'),
    path('UploadTrajectory/',views.uploadtrajectory, name = 'uploadtrajectory'),
    path('DeleteTrajectory/',views.deletetrajectory, name = 'deletetrajectory'),
]