from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete,
    ArticleList, ArticleCreate, ArticleUpdate, ArticleDelete, become_author
)

from . import views

urlpatterns = [
    # Главная страница (новости)
    path('', NewsList.as_view(), name='news_list'),

    # Новости
    path('news/', cache_page(60)(NewsList.as_view()), name='news_list'),
    path('news/<int:pk>/', cache_page(300)(NewsDetail.as_view()), name='news_detail'),
    path('news/search/', cache_page(300)(NewsSearch.as_view()), name='news_search'),
    path('news/create/', cache_page(300)(NewsCreate.as_view()), name='news_create'),
    path('news/<int:pk>/edit/', cache_page(300)(NewsUpdate.as_view()), name='news_edit'),
    path('news/<int:pk>/delete/', cache_page(300)(NewsDelete.as_view()), name='news_delete'),

    # Статьи
    path('articles/', cache_page(300)(ArticleList.as_view()), name='article_list'),
    path('articles/create/', cache_page(300)(ArticleCreate.as_view()), name='article_create'),
    path('articles/<int:pk>/edit/', cache_page(300)(ArticleUpdate.as_view()), name='article_edit'),
    path('articles/<int:pk>/delete/', cache_page(300)(ArticleDelete.as_view()), name='article_delete'),

    path('category/<int:category_id>/', views.category_posts, name='category_posts'),

    # Стать автором
    path('become-author/', become_author, name='become_author'),
]