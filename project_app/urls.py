from django.urls import path
from . import views
# from .views import detail_view

from .views import ExampleList, OtherList
urlpatterns = [
    path('ExampleList', ExampleList.as_view()),

    path('', views.index, name='index'),

    # class based views

    # function based views
    path('function-based-views/create', views.create_view),
    path('function-based-views/list', views.list_view),
    path('function-based-views/<id>', views.detail_view),
    path('function-based-views/<id>/update', views.update_view),
    path('function-based-views/<id>/delete', views.delete_view),

    path('OtherList', OtherList.as_view()),
]
