""" Products urls """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import products as product_views

router = DefaultRouter()
router.register(r'products', product_views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]