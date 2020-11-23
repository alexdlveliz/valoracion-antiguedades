""" Profile serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from valoracion.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """ Profile model serializer """

    biography = serializers.CharField(max_length=500, required=False)

    is_titrator = serializers.BooleanField(required=True)

    class Meta:
        """ Meta Class """
        
        model = Profile
        fields = (
            'id', 'user', 'biography', 'is_titrator'
        )