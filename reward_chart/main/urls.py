from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:chart_id>/points", views.increase_points, name="increase_points"),
    path("<int:chart_id>/redeem", views.redeem, name="redeem"),
]
