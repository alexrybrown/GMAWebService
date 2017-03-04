from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from goals.serializers import GoalSerializer

from goals.models import Goal


class GoalViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = GoalSerializer

    def get_queryset(self):
        if self.request.user.id is not None:
            return Goal.objects.filter(user=self.request.user)
        else:
            return Goal.objects.none()

    def get_serializer_context(self):
        return {'token_id': Token.objects.get(user=self.request.user).pk}
