""" Titration views """

# Django REST Framework
from rest_framework import viewsets

# Serializers
from valoracion.titrations.serializers import TitrationModelSerializer

# Models
from valoracion.titrations.models import Titration


class TitrationViewSet(viewsets.ModelViewSet):
    """ Titration view set """

    serializer_class = TitrationModelSerializer

    def get_queryset(self):
        """ Show titrations """
        queryset = Titration.objects.all()
        return queryset
    
    def create_queryset(self, serializer):
        """ Create titration """

        titration = serializer.save()
        Titration.objects.create(
            profile=titration.profile,
            product=titration.product,
            score=titration.score,
            reference=titration.reference
        )