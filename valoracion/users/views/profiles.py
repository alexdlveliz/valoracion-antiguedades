""" Profile views """

# Django REST Framework
from rest_framework import viewsets

# Serializers
from valoracion.users.serializers import ProfileModelSerializer

# Models
from valoracion.users.models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    """ Profile view set """

    serializer_class = ProfileModelSerializer

    def get_queryset(self):
        """ Show profiles """

        queryset = Profile.objects.all()
        return queryset
    
    def create_queryset(self, serializer):
        """ Create profile """

        profile = serializer.save()
        Profile.objects.create(
            user=profile.user,
            biography=profile.biography,
            is_titrator=profile.is_titrator
        )