from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModuleViewSet, LessonViewSet

router = DefaultRouter()
router.register("modules", ModuleViewSet)
router.register("lessons", LessonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]