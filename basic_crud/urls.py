from django.urls import path
from . import views

app_name = 'ddo'

urlpatterns = [
    path('example', views.example, name="example")
]
