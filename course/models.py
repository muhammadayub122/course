from django.db import models
from user.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)


class StudentCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_studentcourse_user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_studentcourse_course')
    is_paid = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)