
from django.db import models
from course.models import Course

# Create your models here.
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)