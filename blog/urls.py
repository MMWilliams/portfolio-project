from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='details'), #look for an integer then blog ID
] 
    #this is where we should look for files
