from django.http import HttpResponse
from .models import ExampleModel, OtherModel
from django.views.generic.list import ListView
from .forms import ExampleForm
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect


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


def list_view(request):
    context = {"dataset": ExampleModel.objects.all()}
    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {"data": ExampleModel.objects.get(id=id)}
    return render(request, "detail_view.html", context)


def update_view(request, id):
    obj = get_object_or_404(ExampleModel, id=id)
    form = ExampleForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context = {"form": form}

    return render(request, "create_view.html", context)


def delete_view(request, id):
    obj = get_object_or_404(ExampleModel, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/ExampleList")

    return render(request, "delete_view.html")
