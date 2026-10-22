from django.contrib import admin
from .models import Section, Department, Faculty, Subject

# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)

admin.site.register(Subject)
admin.site.register(Department)