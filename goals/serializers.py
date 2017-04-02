from rest_framework import serializers

from goals.models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('user', 'updated_by')

    def create(self, validated_data):
        return Goal.objects.create(user=self.context['request'].user, updated_by=self.context['request'].user,
                                   **validated_data)
