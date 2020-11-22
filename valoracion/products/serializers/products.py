""" Product serializers """

# Django REST Framework
from rest_framework import serializers

# Model
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

    class Meta:
        """ Meta Class """

        model = Product
        fields = (
            'id', 'name', 'description',
            'is_sold'
        )