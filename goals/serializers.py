from rest_framework import serializers
from rest_framework.authtoken.models import Token

from goals.models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('user', 'updated_by')

    def validate(self, attrs):
        token = Token.objects.get(pk=self.context.get("token_id"))
        attrs['user'] = token.user
        return attrs
