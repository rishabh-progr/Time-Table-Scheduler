from django.shortcuts import render
from .models import Section

# Create your views here.
def index(request):
    sections = Section.objects.all().order_by("semester", "name")

    return render(request, "scheduler/index.html", {
        "sections": sections
    })

def section_detail(request, section_id):
    section = get_object_or_404(Section, id=section_id)

    return render(request, "scheduler/section_detail.hml", {
        "section": section
    })