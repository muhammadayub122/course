from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CourseViewSet, StudentCourseViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("courses", CourseViewSet)
router.register("studentcourses", StudentCourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]