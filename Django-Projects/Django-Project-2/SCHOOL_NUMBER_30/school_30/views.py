from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Staff, Vacancy, Sponsors, News, SchoolDocument, Feedback
from .filters import NewsFilter

# Create your views here.
class StaffListView(ListView):
    model = Staff
    template_name = 'staff/list.html'
    context_object_name = 'staff_list'
    paginate_by = 20


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'staff/staff_1.html'
    context_object_name = 'staff_1'


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy.html'
    context_object_name = 'vacancy_list'
    paginate_by = 5


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy/vacancy_1.html'
    context_object_name = 'vacancy_1'


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_1.html'
    context_object_name = 'news_1'


class SponsorsListView(ListView):
    model = Sponsors
    template_name = 'sponsors.html'
    context_object_name = 'sponsors'
    paginate_by = 10


class DocumentsListView(ListView):
    model = SchoolDocument
    template_name = 'documents.html'
    context_object_name = 'documents'
    paginate_by = 10
