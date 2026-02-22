from rest_framework import serializers
from .models import Homework, HomeworkSubmission


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = "__all__"