from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from .models import (
    Games, Staff, Vacancy, Products,
    News, Sponsors, Feedback, Cooperation
)
from .forms import FeedbackForm, CooperationForm

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

class GamesListView(ListView):
    model = Games
    template_name = 'games/list.html'
    context_object_name = 'games'
    paginate_by = 10

class GameDetailView(DetailView):
    model = Games
    template_name = 'games/detail.html'
    context_object_name = 'game'

class StaffListView(ListView):
    model = Staff
    template_name = 'staff/list.html'
    context_object_name = 'staff_members'
    paginate_by = 10

class StaffDetailView(DetailView):
    model = Staff
    template_name = 'staff/detail.html'
    context_object_name = 'staff'

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies/list.html'
    context_object_name = 'vacancies'
    queryset = Vacancy.objects.filter(is_actual='ACTIVE')
    paginate_by = 10

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/detail.html'
    context_object_name = 'vacancy'

class ProductsListView(ListView):
    model = Products
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/detail.html'
    context_object_name = 'product'

class NewsListView(ListView):
    model = News
    template_name = 'news/list.html'
    context_object_name = 'news_list'
    ordering = ['-created_at']
    paginate_by = 10

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'

class SponsorsListView(ListView):
    model = Sponsors
    template_name = 'sponsors/list.html'
    context_object_name = 'sponsors'
    paginate_by = 10

class SponsorDetailView(DetailView):
    model = Sponsors
    template_name = 'sponsors/detail.html'
    context_object_name = 'sponsor'


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/form.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.request.path_info)


class CooperationCreateView(CreateView):
    model = Cooperation
    form_class = CooperationForm
    template_name = 'cooperation/form.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.request.path_info)