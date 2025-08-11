from django.urls import path
from . import views

from .views import ExampleList, OtherList
urlpatterns = [
    path('ExampleList', ExampleList.as_view()),
    path('OtherList', OtherList.as_view()),
    path('', views.index, name='index'),
    path('form', views.create_view),
    # path('test', views.test, name="test"),
]
