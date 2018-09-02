from django.http import HttpResponse
from djnago.template import loader

from .models import Post
# Create your views here.

def index(request):
    template = loader.get_template('jhblog/index.html')

    return HttpResponse(template.render(context, request))
