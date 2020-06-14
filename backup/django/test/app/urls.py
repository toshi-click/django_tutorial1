from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("two", views.twopage, name="twopage")
]
