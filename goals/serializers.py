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

    # def create(self, validated_data):
    #     goal = Goal.objects.create(
    #         user=validated_data.get('user'),
    #         parent_goal=validated_data.get('parent_goal'),
    #         title=validated_data.get('title'),
    #         description=validated_data.get('description'),
    #         comment=validated_data.get('comment'),
    #         expected_completion=validated_data.get('expected_completion'),
    #         finished_at=validated_data.get('finished_at'),
    #         updated_by=validated_data.get('user'),
    #     )
    #     goal.save()
    #     return goal
