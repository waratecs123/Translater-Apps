from django.urls import path
from . import views
from .views import CharacterListView, CharacterDetailView, CharacterCreateView, CharacterUpdateView, CharacterDeleteView
from .views import AttributeListView, AttributeDetailView, AttributeCreateView, AttributeUpdateView, AttributeDeleteView
from .views import InventoryItemListView, InventoryItemDetailView, InventoryItemCreateView, InventoryItemUpdateView, InventoryItemDeleteView
from .views import CharacterListApiView, CharacterDetailApiView, AttributeListApiView, AttributeDetailApiView, InventoryItemListApiView, InventoryItemDetailApiView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Character API",
        default_version='v1',
        description="API documentation for Character management system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('api/', views.CharacterListApiView.as_view(), name='character_list_api'),
    path('<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('<int:pk>/api/', views.CharacterDetailApiView.as_view(), name='character_detail_api'),
    path('create/', views.CharacterCreateView.as_view(), name='character_create'),
    path('<int:pk>/update/', views.CharacterUpdateView.as_view(), name='character_update'),
    path('<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='character_delete'),

    path('attribute/', views.AttributeListView.as_view(), name='attribute_list'),
    path('attribute/api/', views.AttributeListApiView.as_view(), name='attribute_list_api'),
    path('attribute/<int:pk>/', views.AttributeDetailView.as_view(), name='attribute_detail'),
    path('attribute/<int:pk>/api/', views.AttributeDetailApiView.as_view(), name='attribute_detail_api'),
    path('attribute/create/', views.AttributeCreateView.as_view(), name='attribute_create'),
    path('attribute/<int:pk>/update/', views.AttributeUpdateView.as_view(), name='attribute_update'),
    path('attribute/<int:pk>/delete/', views.AttributeDeleteView.as_view(), name='attribute_delete'),

    path('inventory_item/', views.InventoryItemListView.as_view(), name='inventory_item_list'),
    path('inventory_item/api/', views.InventoryItemListApiView.as_view(), name='inventory_item_list_api'),
    path('inventory_item/<int:pk>/', views.InventoryItemDetailView.as_view(), name='inventory_item_detail'),
    path('inventory_item/<int:pk>/api/', views.InventoryItemDetailApiView.as_view(), name='inventory_item_detail_api'),
    path('inventory_item/create/', views.InventoryItemCreateView.as_view(), name='inventory_item_create'),
    path('inventory_item/<int:pk>/update/', views.InventoryItemUpdateView.as_view(), name='inventory_item_update'),
    path('inventory_item/<int:pk>/delete/', views.InventoryItemDeleteView.as_view(), name='inventory_item_delete'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]