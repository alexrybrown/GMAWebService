from django.contrib.auth.models import User

from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(allow_blank=False,
                                             style={'input_type': 'password'},
                                             write_only=True)
    password = serializers.CharField(allow_blank=False, style={'input_type': 'password'})

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'confirm_password',)
        write_only_fields = ('password', 'confirm_password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
