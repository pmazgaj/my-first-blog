"""
Creates API views for shop application
"""
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.api import serializers
from .serializers import ShopSerializer

from shop.models import Shop

__author__ = "Przemek"


def validate_user(request):
    """
    return True if user is superuser or staff, else raise 404
    """
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404

    return True


class ShopListApiView(APIView):
    """
    Get all shops, or create new one.
    View for rest_framework api
    """

    @staticmethod
    def get(request):
        """
        Get api data for all shops, with authenticated login.
        """
        if not validate_user(request):
            shops = Shop.objects.all()
            serializer = ShopSerializer(shops, many=True)

            return Response(serializer.data)


class ShopDetailApiView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'id'
    # lookup_url_kwarg = 'id'


class AuthView(APIView):
    """
    Authentication for post
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]
    serializer_class = serializers.ShopSerializer

    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)
