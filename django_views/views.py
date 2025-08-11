from django.http import HttpResponse
from .models import ExampleModel, OtherModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import ExampleForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse


def index(request):
    return render(request, "django_views/index.html")


class ExampleCreate(CreateView):
    model = ExampleModel
    fields = "__all__"
    template_name = "django_views/function-based-views/create_view.html"
    success_url = "/ExampleList"


class ExampleList(ListView):
    model = ExampleModel


class OtherList(ListView):
    model = OtherModel


def create_view(request):
    context = {}

    form = ExampleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse("function-based-views_list"))

    context['form'] = form
    return render(request, "django_views/function-based-views/create_view.html", context)


def list_view(request):
    context = {"dataset": ExampleModel.objects.all()}
    return render(request, "django_views/function-based-views/list_view.html", context)


def detail_view(request, id):
    context = {"data": ExampleModel.objects.get(id=id)}
    return render(request, "django_views/function-based-views/detail_view.html", context)


def update_view(request, id):
    obj = get_object_or_404(ExampleModel, id=id)
    form = ExampleForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect(reverse("function-based-views_list"))

    context = {"form": form}

    return render(request, "django_views/function-based-views/update_view.html", context)


def delete_view(request, id):
    obj = get_object_or_404(ExampleModel, id=id)
    if request.method == "POST":
        obj.delete()
        # return HttpResponseRedirect("/function-based-views/list")
        return redirect(reverse("function-based-views_list"))

    return render(request, "django_views/function-based-views/delete_view.html")
