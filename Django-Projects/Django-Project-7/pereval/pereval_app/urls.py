from django.urls import path
from .views import SubmitDataView

urlpatterns = [
    path('submitData/', SubmitDataView.as_view(), name='submit-data'),
    path('submitData/<int:pk>/', SubmitDataView.as_view(), name='submit-data-detail'),
]