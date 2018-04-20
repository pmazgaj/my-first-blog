"""
Creates API views for shop application
"""
from django.http import Http404, HttpResponseForbidden
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ShopSerializer

from shop.models import Shop

__author__ = "Przemek"


def validate_user(request):
    """
    return True if user is superuser or staff, else raise 404
    """
    if not request.user.is_superuser or not request.user.is_staff:
        raise HttpResponseForbidden

    return True


class ShopListApiView(APIView):
    """
    Get all shops list.
    View for rest_framework api
    """
    @staticmethod
    def get(request):
        """
        Get api data for all shops, with authenticated login.
        """
        if validate_user(request):
            shops = Shop.objects.all()
            serializer = ShopSerializer(shops, many=True)

            return Response(serializer.data)


class ShopDetailApiView(RetrieveAPIView):
    """
    Get all shops list.
    View for rest_framework api
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if validate_user(request):
            lookup_id = kwargs.get(self.lookup_field, 1)  # try to get shop with given id, if not found - 1
            affected_shop = Shop.objects.filter(id__exact=lookup_id)
            response = Response(affected_shop)
            return response


class AuthView(APIView):
    """
    Authentication for post
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]
    serializer_class = ShopSerializer

    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)
