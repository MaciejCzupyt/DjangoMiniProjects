from django.urls import path
from . import views
# from .views import detail_view

from .views import ExampleList, OtherList
urlpatterns = [
    path('ExampleList', ExampleList.as_view()),
    path('OtherList', OtherList.as_view()),
    path('', views.index, name='index'),
    path('ExampleForm', views.create_view),
    path('<id>', views.detail_view),
    path('<id>/update', views.update_view),
    path('<id>/delete', views.delete_view),
    # path('test', views.test, name="test"),
]
