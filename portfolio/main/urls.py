from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('projects/',views.projects,name='projects'),
    path('languages/',views.languages, name ='languages'),
    path('experience/',views.experience, name ='experience'),
    path('educations/',views.educations, name ='educations'),
    path('achivements/',views.achivements, name ='achivements'),
]