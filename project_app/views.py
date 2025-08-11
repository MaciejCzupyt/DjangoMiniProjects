from django.http import HttpResponse
from .models import ExampleModel, OtherModel
from django.views.generic.list import ListView
from .forms import ExampleForm
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world")


class ExampleList(ListView):
    model = ExampleModel


class OtherList(ListView):
    model = OtherModel


def create_view(request):
    context = {}

    form = ExampleForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


