from datetime import datetime

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

    def update(self, instance, validated_data):
        Goal.objects.update(**validated_data)
        instance = Goal.objects.get(pk=instance.pk)
        instance.updated_by = self.context['request'].user
        instance.last_modified = datetime.now()
        instance.save()
        return instance


class GoalCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('comment',)

    def update(self, instance, validated_data):
        instance = super(GoalCompleteSerializer, self).update(instance, validated_data)
        instance.completed_at = datetime.now()
        return instance
