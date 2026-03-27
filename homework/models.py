from django.db import models
from lesson.models import Lesson
from user.models import User


# Create your models here.
class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="homework/", blank=True, null=True)


class HomeworkSubmission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="submissions/",blank=True, null=True)
    ball = models.IntegerField(default=0)
    is_checked = models.BooleanField(default=False)