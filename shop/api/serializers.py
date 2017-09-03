"""
Create serializers for rest framework
"""

from rest_framework import serializers
from shop.models import Shop, Category

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
