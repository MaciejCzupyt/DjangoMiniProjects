from django.http import HttpResponse
from .models import ExampleModel
from django.views.generic.list import ListView


class ExampleList(ListView):
    model = ExampleModel


def index(request):
    return HttpResponse("Hello world")
