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
    entries = TimetableEntry.objects.filter(
        section=section
    ).select_related("subject", "faculty", "classroom")

    days = TimetableEntry.DAY_CHOICES
    periods = TimetableEntry.PERIOD_CHOICES

    entry_lookup = {
        (entry.day, entry.period): entry
        for entry in entries
    }

    timetable = []

    for period_number, period_label in periods:
        row = {
            "period_label": period_label,
            "cells": []
        }

        for day_code, day_label in days:
            entry = entry_lookup.get((day_code, period_number))

            row["cells"].append({
                "entry": entry
            })

        timetable.append(row)

    return render(request, "scheduler/section_detail.html", {
        "section": section,
        "days": days,
        "timetable": timetable,
    })