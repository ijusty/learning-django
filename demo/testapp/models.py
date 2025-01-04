from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
class TodoItem2(models.Model):
    title = models.CharField(max_length=400)
    completed = models.BooleanField(default=False)
class musicProfile(models.Model):
    title = models.CharField(max_length=250)
    youtubelink = models.CharField(max_length=1000)


class Student(models.Model):
    StudentName = models.CharField(max_length=100)
    
    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshman")
        SOPHOMORE = "SO", _("Sophomore")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }