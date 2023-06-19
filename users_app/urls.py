from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user-home'),
    #path('list', views.home, name='list-user'),
    path('create', views.create, name='add-user'),
    #path('form', views.form, name='display-form')
]