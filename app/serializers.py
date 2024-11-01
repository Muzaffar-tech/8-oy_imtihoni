from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Course, Lesson, Comment, Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    '''
    Kurs uchun serializer
    '''
    class Meta:
        model = Course
        fields = "__all__"

class LessonSerializer(serializers.ModelSerializer):

    '''
    Dars uchun serializer
    '''
    class Meta:
        model = Lesson
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    '''
    Kommentariya uchun serializer
    '''

    class Meta:
        model = Comment
        fields = "__all__"
        depth = 1



class UserRegistrationSerializer(serializers.ModelSerializer):

    '''
    Yangi user yaratish uchun serializer
    '''

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

