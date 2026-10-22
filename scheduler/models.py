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
        return f"{self.first} {self.last} from {self.department}"