from django.core import validators
from django.db import models

# Create your models here.

'''
Kurs uchun model
'''
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    '''
    Dars uchun model
    '''

    name = models.CharField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='lessons/videos/', null=True, blank=True,
                             validators=
                             [
                                 validators.FileExtensionValidator(["mp4", "avi", "wmv", "webm"])
                             ])
    def __str__(self):
        return self.name

class Comment(models.Model):
    '''
    Kommetnariya uchun model
    '''
    text = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Like(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    liked = models.BooleanField()



