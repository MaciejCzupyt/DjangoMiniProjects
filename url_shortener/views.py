import string

from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import UrlData
import random


def url_shortener(request):
    # Required? Purpose?
    if request.method == 'POST':
        form = UrlForm(request.POST or None)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for _ in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            # return redirect(whatever)
    else:
        form = UrlForm()

    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data,
    }

    return render(request, "url_shortener/url_shortener.html", context)


def url_redirect(request, slug):
    data = UrlData.objects.get(slug=slug)
    return redirect(data.url)
