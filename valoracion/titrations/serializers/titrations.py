""" Titration serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from valoracion.titrations.models import Titration


class TitrationModelSerializer(serializers.ModelSerializer):
    """ Titration model serializer """

    score = serializers.FloatField(required=True)

    reference = serializers.CharField(max_length=500, required=False)

    class Meta:
        """ Meta Class """

        model = Titration
        fields = (
            'id', 'profile', 'product',
            'score', 'reference'
        )