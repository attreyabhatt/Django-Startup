from django.shortcuts import render
from .models import Person, Course, Lesson, Section


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
