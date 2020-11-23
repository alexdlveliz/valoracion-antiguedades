""" User serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from valoracion.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer """

    email = serializers.EmailField(required=True)

    username = serializers.CharField()

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    phone_number = serializers.CharField(max_length=17)

    class Meta:
        """ Meta Class """

        model = User
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name', 'phone_number'
        )