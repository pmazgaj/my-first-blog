"""
Create serializers for rest framework
"""

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from shop.models import Shop
from shop.models import Category
# from .serializers import CategorySerializer
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from . import serializers, authentication
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status

__author__ = "Przemek"


class ShopSerializer(serializers.ModelSerializer):
    """
    Serializer for shop (temporary - all fields included)
    """

    class Meta:
        model = Shop
        # fields = ('name', 'description')
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category (temporary - all fields included)
    """

    class Meta:
        model = Category

        fields = '__all__'
