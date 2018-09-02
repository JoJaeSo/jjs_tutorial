from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CreateUserForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'main_index/index.html'


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class ResisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
    
