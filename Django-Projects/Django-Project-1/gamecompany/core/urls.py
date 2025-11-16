from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'glavnoe.html'), name='glavnoe'),

    # Static pages
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),

    # Games
    path('games/', views.GamesListView.as_view(), name='games_list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),

    # Staff
    path('staff/', views.StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail'),

    # Vacancies
    path('vacancies/', views.VacancyListView.as_view(), name='vacancies_list'),
    path('vacancies/<int:pk>/', views.VacancyDetailView.as_view(), name='vacancy_detail'),

    # Products
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # News
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),

    # Sponsors
    path('sponsors/', views.SponsorsListView.as_view(), name='sponsors_list'),
    path('sponsors/<int:pk>/', views.SponsorDetailView.as_view(), name='sponsor_detail'),

    # Forms
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback'),
    path('cooperation/', views.CooperationCreateView.as_view(), name='cooperation'),
]