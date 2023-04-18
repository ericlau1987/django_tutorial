from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # empty means main site
    path('counter', views.counter, name='counter')
]