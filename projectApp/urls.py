from django.urls import path
from . import views

from .views import ExampleList
urlpatterns = [
    path('ExampleList', ExampleList.as_view()),
    path('', views.index, name='index'),
    # path('test', views.test, name="test"),
]
