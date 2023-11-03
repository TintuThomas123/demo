from os import path

from django.contrib.admin import views
from .import views
from django.urls import path
urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
     path('update/<int:id>/',views.update,name='update'),
    path('classbaseview/',views.Tasklistview.as_view(),name='classbaseview'),
    path('cbvdetail/<int:pk>/',views.Taskviewdetail.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]