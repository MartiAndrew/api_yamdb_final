from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.consts import SERVICE_NAME
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value.lower() == SERVICE_NAME:
            raise ValidationError(
                f'Использовать {SERVICE_NAME} в качестве username запрещено.',
            )

        return value


class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio')

    def validate_username(self, value):
        if value.lower() == SERVICE_NAME:
            raise ValidationError(
                f'Использовать {SERVICE_NAME} в качестве username запрещено.',
            )

        return value
