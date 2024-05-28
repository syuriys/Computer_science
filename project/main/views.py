from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Contacts, Feedback, News, AboutProgram, Teacher, Course
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Case, When, Value, IntegerField
from django.db.models.functions import Lower


# Create your views here.
def main(request):
    about_program = AboutProgram.objects.first()
    teachers = Teacher.objects.all()

    paginator = Paginator(teachers, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    active_tab = request.GET.get('active_tab', 'general-info')

    block_order = Case(
        When(block='Природничо-науковий блок', then=Value(1)),
        When(block='Фаховий блок', then=Value(2)),
        When(block='Фахові дисципліни вільного вибору', then=Value(3)),
        When(block='Гуманітарний блок', then=Value(4)),
        default=Value(5),
        output_field=IntegerField()
    )

    courses = Course.objects.all().annotate(
        block_order=block_order).order_by('semester', 'block_order')

    semesters = {i: [] for i in range(1, 9)}
    for course in courses:
        semesters[course.semester].append(course)

    semester_numbers = list(range(1, 9))
    credit_lines = list(range(1, 31))

    paginator = Paginator(list(semesters.items()), 2) 
    page = request.GET.get('page')

    try:
        semesters = paginator.page(page)
    except PageNotAnInteger:
        semesters = paginator.page(1)
    except EmptyPage:
        semesters = paginator.page(paginator.num_pages)

    context = {
        'about_program': about_program,
        'page_obj': page_obj,
        'teachers': teachers,
        'active_tab': active_tab,
        'semesters': semesters,
        'credit_lines': credit_lines
    }
    return render(request, 'main.html', context)


def contacts(request):
    if request.method == 'POST':
        Feedback.objects.create(
            name=request.POST.get('name'),
            surname=request.POST.get('surname'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
            phone_number=request.POST.get('phone_number')
        )
    contacts = Contacts.objects.first()
    return render(request, 'contacts.html', {'contacts': contacts})


def news(request):
    order = request.GET.get('order', '-publication_date')
    all_news = News.objects.all().order_by(order)

    search_query = request.GET.get('search')
    if search_query:
        all_news = all_news.annotate(lower_title=Lower('title')).filter(
            lower_title__icontains=search_query.lower())

    paginator = Paginator(all_news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'order': order,
    }
    return render(request, 'news.html', context)


def news_details(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    images = news_item.images.all()
    return render(request, 'news_details.html', {'news_item': news_item, 'images': images})


