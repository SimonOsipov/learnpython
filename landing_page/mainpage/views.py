from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import (MoscowPythonMeetup, LearnPythonCourse, GraduateProjects,
                     LearnPythonCoursePrices, 
                     Feedback, Curators, GraduateStories)
from datetime import date


def index(request):
    '''Docstring testc'''
    template = loader.get_template('mainpage/index.html')

    # Course data
    # Fixes #3 LearnPythonCourse matching query does not exist.
    try:
        current_course = LearnPythonCourse.objects.latest('course_index')
    except LearnPythonCourse.DoesNotExist:
        current_course = LearnPythonCourse()

    online_prices = LearnPythonCoursePrices.objects.filter(
        course_type='Online').order_by('price_range_price')
    offline_prices = LearnPythonCoursePrices.objects.filter(
        course_type='Offline').order_by('price_range_price')

    # Student projects data
    student_projects = list(GraduateProjects.objects.all())

    # Time for lessons
    lesson_start_time = LearnPythonCourse.objects\
        .all()[:1].get().time_lessons_start
    lesson_end_time = LearnPythonCourse.objects\
        .all()[:1].get().offline_session_end

    # User stories
    graduate_stories_list = list(GraduateStories.objects.all())

    # Curators data
    curators_list = Curators.objects.filter(curator_status=True)

    # Feedback data
    student_feedback = list(Feedback.objects.all())

    context = {
        'course': current_course,
        'projects': student_projects,
        'online_price_ranges': online_prices,
        'offline_price_ranges': offline_prices,
        'lesson_start_time': lesson_start_time,
        'lessons_end_time': lesson_end_time,
        'registration_closes_date': current_course.end_registration_date
        .strftime(
                '%b %d, %Y %H:%M:%S'
            ),
        'student_feedback': student_feedback,
        'curators_list': curators_list,
        'graduate_stories': graduate_stories_list,
        'today': date.today()

    }
    return HttpResponse(template.render(context, request))


def online(request):
    return render(request, 'mainpage/page3759545.html')