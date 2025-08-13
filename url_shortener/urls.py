from django.urls import path
from url_shortener import views

urlpatterns = [
    path('', views.url_shortener, name="url_shortener"),
    path("u/<str:slug>", views.url_redirect, name="redirect")
]
