from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Module, Lesson
from .serializer import ModuleSerializer, LessonSerializer


# Create your views here.
class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer