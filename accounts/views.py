from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts import serializers


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.AccountSerializer

    @detail_route(methods=['get'], authentication_classes=[TokenAuthentication],
                  permission_classes=[IsAuthenticated])
    def info(self, request, pk=None):
        user = Token.objects.get(key=pk).user
        serializer = self.serializer_class(user)
        return Response(serializer.data)
