from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Person(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


TYPE = (("free", "free"), ("paid", "paid"))


class Course(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=2000)
    thumbnail_url = models.CharField(max_length=1000)
    type = models.CharField(
        max_length=20,
        choices=TYPE,
        default='free'
    )
    course_length = models.CharField(max_length=100)
    description_text = models.CharField(max_length=5000, default='Text here')

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


PREVIEW = (("yes", "yes"), ("no", "no"))


class Lesson(models.Model):
    title = models.CharField(max_length=500)
    video_url = models.CharField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    preview = models.CharField(
        max_length=20,
        choices=PREVIEW,
        default='no'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_given = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.content


class Reply(models.Model):
    user_given = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    comment_on = models.ForeignKey(Comment, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.reply_content

