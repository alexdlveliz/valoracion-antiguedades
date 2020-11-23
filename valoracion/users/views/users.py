""" User views """

# Django REST Framework
from rest_framework import viewsets

# Serializers
from valoracion.users.serializers import UserModelSerializer

# Models
from valoracion.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """ User view set """

    serializer_class = UserModelSerializer

    def get_queryset(self):
        """ Show users """

        queryset = User.objects.all()
        return queryset
    
    def create_queryset(self, serializer):
        """ Create user """

        user = serializer.save()
        User.objects.create(
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            phone_number=user.phone_number
        )
        