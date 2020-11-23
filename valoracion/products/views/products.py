""" Product views """

# Django REST Framework
from rest_framework import viewsets

# Serializers
from valoracion.products.serializers import ProductModelSerializer

# Models
from valoracion.products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """ Product view set """

    serializer_class = ProductModelSerializer

    def get_queryset(self):
        """ Restrict list to products not sold """
        queryset = Product.objects.all()

        if self.action == 'list':
            return queryset.filter(is_sold=False)
        return queryset

    def create_queryset(self, serializer):
        """ Create product """

        product = serializer.save()
        Product.objects.create(
            name=product.name,
            description=product.description,
            is_sold=product.is_sold,
            score=product.score
        )
