from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from goals.serializers import GoalSerializer

from goals.models import Goal


class GoalViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}

    @list_route(['get'], url_path='get-future-goals')
    def get_future_goals(self, request):
        goals = request.user.goal_set.filter(future_goal=None).order_by('expected_completion')
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)

    @detail_route(['get'], url_path='get-sub-goals')
    def get_sub_goals(self, request, pk=None):
        goal = self.get_object()
        sub_goals = goal.goal_set.all()
        serializer = GoalSerializer(sub_goals, many=True)
        return Response(serializer.data)

    @detail_route(['post'], url_path='add-sub-goal')
    def add_sub_goal(self, request, pk=None):
        goal = self.get_object()
        serializer = GoalSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(future_goal=goal)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
