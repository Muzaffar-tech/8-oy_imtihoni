from django.urls import include, path
from rest_framework import routers


from .views import CourseApiViewSet, LessonApiViewSet, CommentApiViewSet, RegisterViewSet, LikeApiViewSet

router = routers.DefaultRouter()
router.register('register', RegisterViewSet, basename='register')
router.register("course", CourseApiViewSet)
router.register("lesson", LessonApiViewSet)
router.register("comment", CommentApiViewSet)
router.register('like', LikeApiViewSet)

app_name = "app"

urlpatterns = [
    path('', include(router.urls))
]