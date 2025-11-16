from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .views import StaffListView, StaffDetailView, VacancyListView, VacancyDetailView, NewsListView, NewsDetailView, SponsorsListView, DocumentsListView, Feedback

urlpatterns = [
    path('staff/', StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>', StaffDetailView.as_view(), name='staff_1'),
    path('', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    path('vacancy/', VacancyListView.as_view(), name='vacancy'),
    path('vacancy/<int:pk>', VacancyDetailView.as_view(), name='vacancy_1'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_1'),
    path('documents/', DocumentsListView.as_view(), name='documents'),
    path('sponsors/', SponsorsListView.as_view(), name='sponsors'),
    path('feedback/', TemplateView.as_view(template_name='feedback.html'), name='feedback')
]