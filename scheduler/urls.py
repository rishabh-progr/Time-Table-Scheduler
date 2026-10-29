from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("section/<int:section_id>/", views.section_detail, name="section_detail"),
    path("faculty/<int:faculty_id>/", views.faculty_detail, name="faculty_detail"),
]