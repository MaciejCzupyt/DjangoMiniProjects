import os
import django

# Without this, the script isn't running in Django's context
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from django_views.models import OtherModel

OtherModel.objects.create(
    title="title1",
    description="description1"
).save()
OtherModel.objects.create(
    title="title2",
    description="description2"
).save()
OtherModel.objects.create(
    title="title3",
    description="description3"
).save()
