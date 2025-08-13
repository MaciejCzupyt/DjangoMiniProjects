from .models import ExampleModel, OtherModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import ExampleForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy


def index(request):
    return render(request, "django_views/index.html")

# Class-based views


class OtherCreate(CreateView):
    model = OtherModel
    fields = "__all__"
    template_name = "django_views/class-based-views/create_view.html"
    success_url = reverse_lazy('django_views:class-based-views_list')


class OtherList(ListView):
    model = OtherModel
    template_name = "django_views/class-based-views/list_view.html"


class OtherDetail(DetailView):
    model = OtherModel
    template_name = "django_views/class-based-views/detail_view.html"


class OtherUpdate(UpdateView):
    model = OtherModel
    fields = "__all__"
    template_name = "django_views/class-based-views/update_view.html"
    success_url = reverse_lazy('django_views:class-based-views_list')


class OtherDelete(DeleteView):
    model = OtherModel
    template_name = "django_views/class-based-views/delete_view.html"
    success_url = reverse_lazy('django_views:class-based-views_list')

# Function-based-views


def create_view(request):
    context = {}

    form = ExampleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse("django_views:function-based-views_list"))

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
        return redirect(reverse("django_views:function-based-views_list"))

    context = {"form": form}

    return render(request, "django_views/function-based-views/update_view.html", context)


def delete_view(request, id):
    obj = get_object_or_404(ExampleModel, id=id)
    if request.method == "POST":
        obj.delete()
        # return HttpResponseRedirect("/function-based-views/list")
        return redirect(reverse("django_views:function-based-views_list"))

    return render(request, "django_views/function-based-views/delete_view.html")
