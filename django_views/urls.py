from django.urls import path
from . import views
from .views import OtherList, OtherCreate, OtherDetail, OtherUpdate, OtherDelete

urlpatterns = [
    path('', views.index, name='views_index'),

    # class based views
    path('class-based-views/create', OtherCreate.as_view(), name='class-based-views_create'),
    path('class-based-views/list', OtherList.as_view(), name='class-based-views_list'),
    path('class-based-views/<pk>', OtherDetail.as_view(), name='class-based-views_details'),
    path('class-based-views/<pk>/update', OtherUpdate.as_view(), name='class-based-views_update'),
    path('class-based-views/<pk>/delete', OtherDelete.as_view(), name='class-based-views_delete'),

    # function based views
    path('function-based-views/create', views.create_view, name='function-based-views_create'),
    path('function-based-views/list', views.list_view, name='function-based-views_list'),
    path('function-based-views/<id>', views.detail_view, name='function-based-views_details'),
    path('function-based-views/<id>/update', views.update_view, name='function-based-views_update'),
    path('function-based-views/<id>/delete', views.delete_view, name='function-based-views_delete'),
]
