from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Shobhit", views.Shobhit, name="Shobhit"),
    path("harry", views.harry, name="harry"),
    path("mike", views.mike, name="mike")
    ]