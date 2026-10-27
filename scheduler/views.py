from django.shortcuts import render, get_object_or_404
from django.db.models import Case, When, Value, IntegerField
from .models import Section, TimetableEntry

# Create your views here.
def index(request):
    sections = Section.objects.all().order_by("semester", "name")

    return render(request, "scheduler/index.html", {
        "sections": sections
    })

def section_detail(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    entries = TimetableEntry.objects.filter(section=section).annotate(
        day_order=Case(
            When(day="MON", then=Value(1)),
            When(day="TUE", then=Value(2)),
            When(day="WED", then=Value(3)),
            When(day="THU", then=Value(4)),
            When(day="FRI", then=Value(5)),
            When(day="SAT", then=Value(6)),
            output_field=IntegerField(),
        )
    ).select_related("subject", "faculty", "classroom").order_by("day", "period")

    return render(request, "scheduler/section_detail.html", {
        "section": section,
        "entries": entries
    })