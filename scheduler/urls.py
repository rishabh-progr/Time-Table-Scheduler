from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("firstYear/", views.firstYear, name="firstYear"),
    path("secondYear/", views.secondYear, name="secondYear"),
    path("thirdYear/", views.thirdYear, name="thirdYear"),
    path("forthYear/", views.forthYear, name="forthYear")
]