from django.urls import path
from . import views

urlpatterns = [
    path('q/',views.index, name='home')
]