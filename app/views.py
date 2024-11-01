from django.core.exceptions import PermissionDenied
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User



from .models import Course, Lesson, Comment
from .serializers import CourseSerializer, LessonSerializer, CommentSerializer, UserRegistrationSerializer

# Create your views here.


class RegisterViewSet(ModelViewSet):
    '''
    Bu yerda Registret uchun viewset yozilgan
    '''

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    http_method_names = ['post']

    '''
    Yangi User yaratish uchun create methodi
    '''
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ro'yxatdan muvaffaqiyatli o'tdingiz"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseApiViewSet(ModelViewSet):
    '''
    Bu Kurs viewseti bo'lib, bu viewsetda qidirish, tartiblash, ruxsatlar yozilgan
    '''

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'start_date', 'name']
    search_fields = ['name', 'description']





class LessonApiViewSet(ModelViewSet):
    '''
    Bu Dars uchun viewset bo'lib, bu viewsetda qidirish, tartiblash, ruxsatlar yozilgan
    '''

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'date', 'name']
    search_fields = ['pk', 'name']


class CommentApiViewSet(ModelViewSet):
    '''
    Bu Kommentariya qoldirish viewseti bo'lib, bu viewsetda qidirish, tartiblash, ruxsatlar yozilgan
    '''

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk']
    search_fields = ['pk', 'text']
    '''
    Bu method versialash uchun yozilgan (Commentariya qismi v2 da bor)
    '''
    def get_queryset(self):
        if self.request.version == "v2":
            return Comment.objects.all()
        else:
            return None


    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("Faqat o'zingizning kommentlaringizni o'chira olasiz.")

