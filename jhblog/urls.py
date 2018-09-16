from django.urls import path

from . import views

app_name="jhblog"
urlpatterns = [
    path('', views.index, name='index'),
    path('post_new', views.post_new, name='post_new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit')
]