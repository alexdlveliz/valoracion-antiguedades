""" User urls """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views
from .views import profiles as profile_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
router.register(r'profiles', profile_views.ProfileViewSet, basename='profiles')

urlpatterns = [
    path('', include(router.urls))
]