from django.urls import path
from . import views
# from .views import detail_view

from .views import ExampleList, OtherList
urlpatterns = [
    path('ExampleList', ExampleList.as_view()),

    path('', views.index, name='views_index'),

    # class based views

    # function based views
    path('function-based-views/create', views.create_view, name='function-based-views_create'),
    path('function-based-views/list', views.list_view, name='function-based-views_list'),
    path('function-based-views/<id>', views.detail_view, name='function-based-views_details'),
    path('function-based-views/<id>/update', views.update_view, name='function-based-views_update'),
    path('function-based-views/<id>/delete', views.delete_view, name='function-based-views_delete'),

    path('OtherList', OtherList.as_view()),
]
