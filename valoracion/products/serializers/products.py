""" Product serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from valoracion.products.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    """ Product model serializer """
    
    name = serializers.CharField(
        required=True,
        max_length=140
    )

    description = serializers.CharField(
        required=False,
        max_length=500   
    )

    is_sold = serializers.BooleanField(default=False)

    score = serializers.FloatField(default=3.0, required=False)

    class Meta:
        """ Meta Class """

        model = Product
        fields = (
            'id', 'name', 'description',
            'score', 'is_sold'
        )