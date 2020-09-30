from django.shortcuts import render, redirect
from .models import Person, Course, Lesson, Section
from .forms import UserRegistrationForm
import json


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
    context = {
        'current_lesson': lesson,
        'course_obj': course,
        'lessons': lessons,
        'sections': sections,
    }
    return render(request, 'mysite/lesson_details.html', context)


def blog(request):
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
            print(username)
            return redirect('courses')
        else:
            error_json = json.loads(form.errors.as_json())
            errors = error_json["password2"][0]['message']
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
