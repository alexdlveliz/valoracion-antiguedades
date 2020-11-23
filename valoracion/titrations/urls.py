""" Titration urls """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import titrations as titration_views

router = DefaultRouter()
router.register(r'titrations', titration_views.TitrationViewSet, basename='titration')

urlpatterns = [
    path('', include(router.urls))
]