from django.urls import path

from . import views

urlpatterns = [
     path('input/', views.index, name='index'),
     path('multi/', views.mulitiplication, name='multi'),
     path('history/', views.history, name='history'),
     
]
