from django.urls import path

from . import views

app_name = 'visits'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:page>', views.index, name='index'),
]