from django.urls import path
from . import views

urlpatterns = [
    path('phonetic/', views.index, name='index'),
]
