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
class Seller(models.Model):
    StudentName = models.CharField(max_length=100)
    
    class YearInUniv(models.TextChoices):
        firstCourse = "1", _("1 курс")
        secondCourse = "2", _("2 курс")
        thirdCourse = "3", _("3 курс")
        fourthCourse = "4", _("4 курс")
        fifthCourse = "5", _("5 курс")

    year_in_university = models.CharField(
        max_length=1,
        choices=YearInUniv,
        default=YearInUniv.firstCourse,
    )

    def is_upperclass(self):
        return self.year_in_university in {
            self.YearInUniv.firstCourse,
            self.YearInUniv.fifthCourse,
        }