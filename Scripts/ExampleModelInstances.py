import os
import django

# Without this, the script isn't running in Django's context
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

# this should not be at the top, despite what IDEs say
from django_views.models import ExampleModel

ExampleModel.objects.create(
    title="title1",
    description="description1"
).save()
ExampleModel.objects.create(
    title="title2",
    description="description2"
).save()
ExampleModel.objects.create(
    title="title3",
    description="description3"
).save()
