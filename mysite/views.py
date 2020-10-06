from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegistrationForm
import json
from django.contrib.auth import authenticate, login
from utilities import *


def index(request):
    return render(request, 'mysite/index.html')


def courses(request):
    course_list = Course.objects.all()
    context = {
        'courses': course_list
    }
    return render(request, 'mysite/courses.html', context)


def courses_detailed(request, num):
    course = Course.objects.get(id=num)
    sections = Section.objects.filter(course=course)
    lessons = Lesson.objects.filter(course=course)

    context = {
        'course_id': num,
        'course_obj': course,
        'lessons': lessons,
        'sections': sections,
    }
    return render(request, 'mysite/course_details.html', context)


def lessons_detailed(request, num, num1):
    course = Course.objects.get(id=num)
    sections = Section.objects.filter(course=course)
    lessons = Lesson.objects.filter(course=course)
    lesson = Lesson.objects.get(id=num1)
    comments = Comment.objects.filter(lesson=lesson)

    if request.method == 'POST':
        comment = request.POST.get('comment')

        comment_info = Comment(user_given=request.user, lesson=lesson, content=comment)
        comment_info.save()

    context = {
        'current_lesson': lesson,
        'course_obj': course,
        'lessons': lessons,
        'sections': sections,
        'comments': comments,
    }
    return render(request, 'mysite/lesson_details.html', context)


def blog(request):
    subscribe(request)
    return render(request, 'mysite/blog.html')


def pricing(request):
    return render(request, 'mysite/pricing.html')


def optin(request):
    if request.method == 'POST':
        name_r = request.POST.get('fname')
        country_r = request.POST.get('country')
        email_r = request.POST.get('email')

        info = Person(name=name_r, country=country_r, email=email_r)
        info.save()
        opt = True
        context = {'optedin': opt}
        return render(request, 'mysite/optin.html', context)
    else:
        return render(request, 'mysite/optin.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('courses')

        else:
            error_json = json.loads(form.errors.as_json())
            print(error_json)
            try:
                errors = error_json["password2"][0]['message']
            except:
                errors = error_json["username"][0]['message']
            form = UserRegistrationForm()

            context = {
                'form': form,
                'errors': errors,
            }

            return render(request, 'mysite/signup.html', context)

    else:
        form = UserRegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'mysite/signup.html', context)


def profile(request):
    return render(request, 'mysite/profile.html')
