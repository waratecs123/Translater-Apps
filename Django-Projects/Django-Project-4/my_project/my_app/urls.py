from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-email/', ConfirmEmailView.as_view(), name='confirm_email'),
    path('', AdvertListView.as_view(), name='advert_list'),
    path('adverts/create/', AdvertCreateView.as_view(), name='advert_create'),
    path('adverts/<int:pk>/', AdvertDetailView.as_view(), name='advert_detail'),
    path('adverts/<int:pk>/edit/', AdvertUpdateView.as_view(), name='advert_edit'),
    path('adverts/<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert_delete'),
    path('adverts/<int:pk>/response/', ResponseCreateView.as_view(), name='response_create'),
    path('my-responses/', UserResponsesView.as_view(), name='response_list'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
    path('responses/<int:pk>/accept/', ResponseAcceptView.as_view(), name='response_accept'),
    path('responses/<int:pk>/delete/', ResponseDeleteView.as_view(), name='response_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
