from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Section(models.Model):
    semester = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=1)
    subjects = models.ManyToManyField(Subject, blank=True, related_name="sections")

    def __str__(self):
        return f"{self.semester} Semester {self.name}"

class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Department of {self.name}"

class Faculty(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="members")
    subjects = models.ManyToManyField(Subject, blank=True, related_name="faculty")

    def __str__(self):
        return f"{self.first} {self.last} ({self.department})"

class Classroom(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Classroom: {self.name}"

class TimetableEntry(models.Model):
    DAY_CHOICES = [
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
    ]
    PERIOD_CHOICES = [
        (i, f"Period {i}") for i in range(1, 8)
    ]
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    period = models.PositiveSmallIntegerField(choices=PERIOD_CHOICES)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name="timetable_entries")
    classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT, related_name="timetable_entries")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="timetable_entries")
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name="timetable_entries")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["section", "day", "period"],
                name="unique_section_slot"
            ),
            models.UniqueConstraint(
                fields=["faculty", "day", "period"],
                name="unique_faculty_slot"
            ),
            models.UniqueConstraint(
                fields=["classroom", "day", "period"],
                name="unique_classroom_slot"
            ),
        ]

    def __str__(self):
        return (
            f"{self.section} | {self.day} | Period {self.period} "
            f"| {self.subject} | {self.faculty}"
        )