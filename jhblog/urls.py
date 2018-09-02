from django.urls import path

from . import views

app_name="jhblog"
urlpatterns = [
    path('', views.index, name='index'),
]