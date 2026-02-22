from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Homework, HomeworkSubmission
from .serializer import HomeworkSerializer, HomeworkSubmissionSerializer

# Create your views here.

class HomeworkViewSet(ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class HomeworkSubmissionViewSet(ModelViewSet):
    queryset = HomeworkSubmission.objects.all()
    serializer_class = HomeworkSubmissionSerializer